<?php
namespace app\controller;

use app\BaseController;
use think\facade\View;
use think\facade\Request;


class Admin extends BaseController
{
    public function index()
    {
        return View::fetch();
    }
    public function upload()
    {
        //判断是否是POST请求,如果是处理上传逻辑
        if (request()->isPost()){
            //接收文件上传类型
            $type = request()->param('type','','trim');
            $name = request()->param('name','','trim');
            //获取表单上传文件
            $file = request()->file('file');
            //组装文件保存目录
            $upload_dir = '/'.$type.'/'.$name;

            try {
                //从config/upload.php配置文件中读取允许上传的文件后缀和大小
                $suffix_config = config('upload.suffix_arr');
                $size_config = config('upload.size_arr');
                
                if (empty($size_config[$type]) || empty($size_config[$type])){
                    return false;
                }else{
                    $suffix = $suffix_config[$type];
                    $size = $size_config[$type];
                }

                //验证器验证上传的文件
                validate(['file'=>[
                    //限制文件大小
                    'fileSize'      =>  $size * 1024 * 1024,
                    //限制文件后缀
                    'fileExt'       =>  $suffix
                ]],[
                    'file.fileSize' =>  '上传的文件大小不能超过'.$size.'M',
                    'file.fileExt'  =>  '请上传后缀为:'.$suffix.'的文件'
                ])->check(['file'=>$file]);

                //上传文件到本地服务器
                $filename = \think\facade\Filesystem::disk('public')->putFile($upload_dir, $file);

                if ($filename){
                    $src = '/public/storage/'.$filename;
                    return json(['code'=>1,'result'=>$src]);
                }else{
                    return json(['code'=>0,'msg'=>'上传失败']);
                }

            }catch (ValidateException $e){
                return json(['code'=>0,'msg'=>$e->getMessage()]);
            }

        }else{
            return json(['code'=>0,'msg'=>'非法请求']);
        }
    }
}
