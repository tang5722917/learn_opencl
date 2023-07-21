'''
Author: Donald duck tang5722917@163.com
Date: 2023-07-20 17:09:46
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2023-07-20 17:39:04
FilePath: \test\opencl_test.py
Description: 安装pyopencl
Copyright (c) 2023 by Donald duck email: tang5722917@163.com, All Rights Reserved.
'''
import pyopencl as cl
print("CL_VERSION:",cl.VERSION)
print(cl.get_cl_header_version())
platforms = cl.get_platforms()
print("平台数量:"+str(len(platforms)))
for plat in platforms:
    print(plat.get_info(cl.platform_info.NAME))
    print(plat.get_info(cl.platform_info.EXTENSIONS))
    print(plat.get_info(cl.platform_info.PROFILE))
    print(plat.get_info(cl.platform_info.VENDOR))
    print(plat.get_info(cl.platform_info.VERSION))

    devices = plat.get_devices(cl.device_type.ALL)
    print("-- device num:",len(devices))
    for device in devices:
        print("---- DEVICE NAME:",device.get_info(cl.device_info.NAME))
        print("---- OPENCL_C_VERSION:",device.get_info(cl.device_info.OPENCL_C_VERSION))
        print("---- DEVICE VENDOR:",device.get_info(cl.device_info.VENDOR))
        print("---- OPENCL VERSION:",device.get_info(cl.device_info.VERSION))
        print("---- DRIVER_VERSION:",device.get_info(cl.device_info.DRIVER_VERSION))
        print("---- MAX_WORK_GROUP_SIZE:",device.get_info(cl.device_info.MAX_WORK_GROUP_SIZE))
        print("---- MAX_COMPUTE_UNITS:",device.get_info(cl.device_info.MAX_COMPUTE_UNITS))
        print("---- MAX_WORK_ITEM_SIZES:",device.get_info(cl.device_info.MAX_WORK_ITEM_SIZES))
        print("---- LOCAL_MEM_SIZE:",device.get_info(cl.device_info.LOCAL_MEM_SIZE))
