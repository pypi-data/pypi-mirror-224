import json
import numpy as np

class SVCOCam:
    def __init__(self, data, cam_name, down=False):
        cam = data
        self.name = cam_name
        self.eps = 1e-6
        if "ImgSize" in cam.keys() :

            self.width = cam["ImgSize"][0]
            self.height = cam["ImgSize"][1]
        else:
            self.width = cam["intrinsic_param"]["camera_width"]
            self.height = cam["intrinsic_param"]["camera_height"]
        self.pixel2cam_pol_len = int(cam["intrinsic_param"]["cam2world_len"])
        self.pixel2cam_pol = cam["intrinsic_param"]["cam2world"]
        self.cam2pixel_pol_len = int(cam["intrinsic_param"]["world2cam_len"])
        self.cam2pixel_pol = cam["intrinsic_param"]["world2cam"]
        self.A = np.eye(2)
        self.A[0][1] = cam["intrinsic_param"]["affine_e"]
        self.A[1][0] = cam["intrinsic_param"]["affine_d"]
        self.A[1][1] = cam["intrinsic_param"]["affine_c"]
        self.B = np.array(cam["intrinsic_param"]["center"])
        # 倒装补偿
        if down:
            self.B[0] = self.width - 1 - self.B[0]
            self.B[1] = self.height - 1 - self.B[1]

    def cam2pixel(self, Pc):
        Pc = np.array(Pc).reshape(3, -1)
        norm = np.sqrt(np.sum(Pc[:2] * Pc[:2], 0))
        norm = np.where(norm == 0, self.eps, norm)
        theta = np.arctan2(Pc[2] * -1,
                           norm)  # * -1 , because z arrow is negative, x/z instead of z/x if because of 90 - theat
        f = np.poly1d(self.cam2pixel_pol[::-1])
        rho = f(theta)  # g_theta
        xy = (Pc[0:2] * rho / norm).reshape(2, -1)
        p = self.A.dot(xy) + self.B.reshape(2, 1)
        return p
    def cam2pixel2(self, Pc):
        Pc = np.array(Pc).reshape(3, -1)
        norm = np.sqrt(np.sum(Pc[:2] * Pc[:2], 0))
        norm = np.where(norm == 0, self.eps, norm)
        theta = np.arctan2(Pc[2] * -1,
                        norm)  # * -1 , because z arrow is negative, x/z instead of z/x if because of 90 - theat
        rho = np.polyval(self.cam2pixel_pol[::-1], theta)  # g_theta
        xy = (Pc[0:2] * rho / norm).reshape(2, -1)
        p = self.A.dot(xy) + self.B.reshape(2, 1)
        return p
    def pixel2cammy(self, p, depth):
        p -= self.B.reshape(2, 1)
        xy = np.linalg.inv(self.A).dot(p)
        norm = np.sqrt(np.sum(xy * xy, 0))
        norm = np.where(norm == 0, self.eps, norm)
        rho = np.arctan2(depth, norm)
        f = np.poly1d(self.pixel2cam_pol[::-1])
        theat = f(rho)  # g_theta
        xy_cam = (xy * theat / norm).reshape(2, -1)
        xyz_cam = np.concatenate([xy_cam, np.expand_dims(depth, 0)], axis=0)
        return xyz_cam

   

    def pixel2cam2(self, p, depth, gt):
        """vector form: p is a 2*N vector"""
        """vector form: depth is a 1*N vector"""
        """Given a pixel point, return its 3D coordinate in unit sphere"""
        if len(p) != 2:
            p = p.transpose()
        m = np.linalg.inv(self.A).dot(p - self.B.reshape((2, 1)))
        rho = np.sqrt(np.sum(m * m, 0))
        f = np.poly1d(self.pixel2cam_pol[::-1])  # rd to z
        # 【大坑：注意np.poly系数从高到低】
        z = f(rho)
        w = np.concatenate([m[0], m[1], z]).reshape(3, -1)
        norm_w = np.sqrt(np.sum(w * w, 0))
        # 这里求出的w是在omni坐标系下的坐标，还需进行omni坐标系与相机一般相机坐标系的变换
        w[2] *= -1
        # return w
        w /= w[2]
        return w * depth


    def cal_remap_svc(self, fc=0.2, width=1920, height=1300):
        
        Xs, Ys = np.mgrid[-height / 2: height / 2, -width / 2: width / 2]
        Xs, Ys = Xs.reshape(-1), Ys.reshape(-1)
        Zs = np.zeros(width * height)
        plan_pts = np.concatenate([Xs, Ys, Zs]).reshape(3, -1)
        R = np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]])
        t = np.array([0, 0, width * fc])
        cam_pts = R.dot(plan_pts) + t.reshape(3, -1)
        p = self.cam2pixel2(cam_pts)
        #transPose_p = np.transpose(p)
        x_map=p[0,:]
        y_map=p[1,:]
        x_map=x_map.reshape(height,width)
        y_map=y_map.reshape(height,width)
        #project_img = self.bilinear_interpolation(img, transPose_p).reshape(height, width , 3)
        return x_map.astype(np.float32, order='C'),y_map.astype(np.float32, order='C')
        
def choose_ts(can_json_file, sync_frames, is_dlb):
    if is_dlb:
        diff=0.005
    else:
        diff=0.01
    with open(can_json_file,'r') as f:
        speed_info=json.load(f)

    potential_frame=speed_info['vehicle_speed']['timestamp']
    select_frame_list=np.array(sync_frames)[0,:]
    select_index1=0
    select_index2=0
    speed_index_list=[]
    frame_index_list=[]
    while select_index1<len(select_frame_list) and select_index2<len(potential_frame):

        if abs(select_frame_list[select_index1]-potential_frame[select_index2])<diff:
            speed_index_list.append(select_index2)
            frame_index_list.append(select_index1)
            select_index1+=1
            select_index2+=1
        elif select_frame_list[select_index1]>potential_frame[select_index2]:
            select_index2+=1
        else:
            select_index1+=1

    potential_frame_speed=np.array(speed_info['vehicle_speed']['data'])[speed_index_list]
    potential_index=np.argmin(potential_frame_speed)
    return sync_frames[frame_index_list[potential_index]]

def preprocess(sensor_pair, im0, im1):
    fov=fov_pair[sensor_pair]
    roi_single=roi[sensor_pair]
    x0, x1, y0, y1  = roi_single[0]
    x1_0,x1_1,y1_0,y1_1=roi_single[1]
    x0, x1, y0, y1  = int(x0*fov[0]), int(x1*fov[0]), int(y0*fov[0]), int(y1*fov[0])
    x1_0,x1_1,y1_0,y1_1  = int(x1_0*fov[1]), int(x1_1*fov[1]), int(y1_0*fov[1]), int(y1_1*fov[1])
    new_im0 = im0[x0:x1, y0:y1]
    new_im1 = im1[x1_0:x1_1,y1_0:y1_1]
    return new_im0, new_im1
