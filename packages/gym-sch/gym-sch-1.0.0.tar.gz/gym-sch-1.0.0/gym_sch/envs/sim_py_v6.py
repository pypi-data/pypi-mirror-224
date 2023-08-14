

import simpy
import numpy as np
import sys
import copy

# np.random.seed(10)

global go_to_unload_point_vehical_num  # 用于保存每条卸载道路上经过的车辆个数
global go_to_excavator_vehical_num  # 用于保存每条装载道路上的经过的车辆总个数

global walking_go_to_unload_point_vehical_num  # 卸载道路上正在行走的车辆个数
global walking_go_to_excavator_vehical_num  # 装载道路上正在行走的车辆个数

global reach_excavator_time_list  # 驶往挖机矿卡预期抵达时间
global reach_dump_time_list  # 驶往卸点预期抵达时间

global loading_in_excavator_vehical_num  # 挖机装车数
global unloading_in_unload_point_vehical_num  # 卸点卸车数

global wating_in_excavator_vehical_num  # 挖机排队等待装载矿卡数
global wating_in_unload_point_vehical_num  # 卸点排队等待卸载矿卡数

global excavator_loaded_vehicle_num  # 挖机完成装载的车次数
global dump_loaded_vehicle_num  # 卸点完成卸载的车次数

global waiting_vehicle_loaded_time  # 完成所有排队等待车辆装载时间
global waiting_vehicle_unloaded_time  #  完成所有排队等待车辆卸载时间

global dump_available_time  # 卸点最近一次可用时间
global shovel_available_time  # 挖机最近一次可用时间
global truck_available_time  # 矿卡最近一次可用时间

global real_shovel_mass  # 挖机实际装载量
global real_dump_mass  # 卸点实际卸载量

global last_real_shovel_mass  # 上一次调度任务挖机实际装载量
global last_real_dump_mass  # 上一次调度任务卸点实际卸载量

global truck_stage  # 标记矿卡位于哪个阶段（0：空运阶段，1：装载阶段，2：重运阶段， 3：卸载阶段）

global cost  # 记录燃油消耗

global recording  # 数据统计{时间(min), 产量(tonnes), 油耗(liters)}

# 开始行走 -> 行走结束(开始等待) -> 接受服务
global process_start_time  # 矿卡执行当前行走任务的起始时间
global waiting_start_time  # 矿卡开始等待时间
global service_start_time  # 矿卡执行卸载或装载的起始时间

global truck_location  # 矿卡当前位置

global request_truck  # 当前请求调度矿卡

global truck_process  # 矿卡当前任务持续时间

global next_dest  # 矿卡下一目的地

global action_time  # 调度下发时间

global truck_waiting  # 车辆等待时间
global truck_waiting_from_last_act  # 车辆自上一次动作到当前动作等待时间

global truck_task  # 车辆当前任务, 0-空载运输, 1-装载等待, 2-正在装载, 3-重载运输, 4-卸载等待

global request_id  # 请求编号 1-请求调度, 2-行走结束

global goto_excavator_traffic_flow_num  # 驶往挖机各运输路线实际车次
global goto_dump_traffic_flow_num  # 驶往卸点各运输路线实际车次

global load_start_time  # 挖机开始装载时间
global unload_start_time  # 卸点开始卸载时间

global load_end_time  # 挖机结束装载时间
global unload_end_time  # 卸点结束装载时间

global rl_truck    # agent 调度的车辆

global rl_allow    # 是否允许 agent 调度车辆

global rl_evaluate    # agent 测试模式

global heu_rpm    # 启发式调度经验池

global heu_action    # 启发式调度动作

global heu_action_time    # 启发式调度时间

global is_legal    # 动作是否合法

episode = 0

class GlobalVar:
    # 班次时间(min)
    T = 480

    # 矿卡载重(吨)
    payload = 220

    # 矿卡数量
    truck_num = 60

    # 电铲数量
    n = 8
    # 卸点数量
    m = 6

    # 矿卡平均行驶速度
    empty_speed = 25
    heavy_speed = 22

    # 各路线距离
    dis = [[2.41,   6.51,  10.86, 11.16,  7.94,   11.58,  14.7,  6.7],
           [10.82,  8.07,  5.05,  1.66,   11.51,  2.87,   11.4,  11.11],
           [6.28,   2.79,  10.48, 9.59,   10.41,  11.42,  3.96,  5.17],
           [9.06,   9.4,   10.1,  13.93,  5.97,   10.25,  5.33,  5.46],
           [13.23,  12.14, 5.95,  10.7,   7.21,   3.89,   14.65, 7.87],
           [14.63,  4.01,  10.77, 6.11,   13.76,  6.08,   12.73, 12.9]]

    # 电铲装载速度&卸点卸载速度（吨/时）
    load_capacity = np.array([2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000])
    unload_capacity = np.array([2375, 2375, 2375, 2375, 2375, 2375])

    # 各挖机/卸点目标产量
    dump_target_mass = np.array([15000, 15000, 15000, 15000, 15000, 15000])
    shovel_target_mass = np.array([15000, 15000, 15000, 15000, 15000, 15000, 15000, 15000])

    # 矿卡空载行驶能耗
    empty_power = 85
    # 矿卡重载行驶能耗
    heavy_power = 150
    # 矿卡空转能耗
    idle_power = 40
    # 电铲闲置能耗

    shovel_idle_power = [6.6, 9.5, 9.5, 6.6, 6.6, 9.5, 9.5, 6.6]
    shovel_work_power = [117, 130, 130, 117, 117, 130, 130, 117]

    # 速度油耗关系(速度:km/h, 节油系数:%)
    fuel_speed_empty = [[22.5, 0.2], [23, 0.18], [23.5, 0.17], [24, 0.15], [24.5, 0.11], [25, 0.0]]
    fuel_speed_heavy = [[19.5, 0.2], [20, 0.18], [20.5, 0.17], [21, 0.15], [21.5, 0.11], [22, 0.0]]

    # 各路线空载行驶时间（min）
    com_time = 60 * np.array(dis) / empty_speed
    go_time = 60 * np.array(dis) / heavy_speed

    # 电铲装载时间&卸点卸载时间（min）
    loading_time = np.round(60 * (payload) / load_capacity, 3)
    unloading_time = np.round(60 * (payload) / unload_capacity, 3)

    # 装载及卸载时间维度扩展
    loading_time_dims = np.expand_dims(loading_time, 0).repeat(m, axis=0)
    unloading_time_dims = np.expand_dims(unloading_time, 1).repeat(n, axis=1)

    @staticmethod
    def get_para(name):
        if name == 'T&p':
            return GlobalVar.T, GlobalVar.payload
        elif name == 'mnt':
            return GlobalVar.m, GlobalVar.n, GlobalVar.truck_num
        elif name == 'time':
            return GlobalVar.com_time, GlobalVar.go_time, GlobalVar.loading_time, GlobalVar.unloading_time
        elif name == 'energy':
            return GlobalVar.empty_power, GlobalVar.heavy_power, GlobalVar.idle_power, \
                   GlobalVar.shovel_idle_power, GlobalVar.shovel_work_power
        elif name == 'dis':
            return GlobalVar.dis
        elif name == 'fuel_speed':
            return GlobalVar.fuel_speed_empty, GlobalVar.fuel_speed_heavy
        elif name == 'capacity':
            return GlobalVar.load_capacity, GlobalVar.unload_capacity
        elif name == 'target':
            return GlobalVar.shovel_target_mass, GlobalVar.dump_target_mass
        elif name == 'speed':
            return GlobalVar.empty_speed, GlobalVar.heavy_speed


def set_para_list(para_list):
    GlobalVar.n = para_list["shovels"]

    GlobalVar.m = para_list["dumps"]

    GlobalVar.dis = np.array(para_list["rout_distance"])

    GlobalVar.payload = para_list["payload"]

    GlobalVar.truck_num = para_list["truck_num"]

    GlobalVar.load_capacity = np.array(para_list["load_capacity"])

    GlobalVar.unload_capacity = np.array(para_list["unload_capacity"])

    GlobalVar.dump_target_mass = np.array(para_list["dump_target_mass"])

    GlobalVar.shovel_target_mass = np.array(para_list["shovel_target_mass"])

    # 各路线空载行驶时间（min）
    GlobalVar.com_time = 60 * np.array(GlobalVar.dis) / GlobalVar.empty_speed
    GlobalVar.go_time = 60 * np.array(GlobalVar.dis) / GlobalVar.heavy_speed

    # 电铲装载时间&卸点卸载时间（min）
    GlobalVar.loading_time = np.round(60 * (GlobalVar.payload) / GlobalVar.load_capacity, 3)
    GlobalVar.unloading_time = np.round(60 * (GlobalVar.payload) / GlobalVar.unload_capacity, 3)

    # 装载及卸载时间维度扩展
    GlobalVar.loading_time_dims = np.expand_dims(GlobalVar.loading_time, 0).repeat(GlobalVar.m, axis=0)
    GlobalVar.unloading_time_dims = np.expand_dims(GlobalVar.unloading_time, 1).repeat(GlobalVar.n, axis=1)


##############################
#  仿真参数配置，整个仿真的基本单位是分钟
##############################
T, payload = GlobalVar.get_para("T&p")
dumps, shovels, truck_num =GlobalVar.get_para("mnt")
com_time, go_time, loading_time, unloading_time = GlobalVar.get_para("time")
dis = GlobalVar.get_para("dis")
fuel_speed_empty, fuel_speed_heavy = GlobalVar.get_para("fuel_speed")
(
    empty_power,
    heavy_power,
    idle_power,
    shovel_idle_power,
    shovel_work_power,
) = GlobalVar.get_para("energy")
shovel_target_mass, dump_target_mass = GlobalVar.get_para("target")
empty_speed, heavy_speed = GlobalVar.get_para("speed")


def truck_schedule_send_post_start(truck_id: int, start_area: int, task_id: int, env: object):
    global shovel_available_time
    global truck_available_time
    global real_shovel_mass
    global last_real_shovel_mass
    target = np.argmax(
        1000 * (1 - real_shovel_mass / shovel_target_mass)
        / (np.maximum(shovel_available_time, env.now + com_time[start_area][:]) - env.now))
    shovel_available_time[target] = max(shovel_available_time[target], truck_available_time[truck_id] + com_time[
        start_area][target])
    truck_available_time[truck_id] = shovel_available_time[target]
    last_real_shovel_mass = copy.deepcopy(real_shovel_mass)
    real_shovel_mass[target] += payload
    return target


def truck_schedule_send_post(start_area: int, task_id: int, dispatch_method=0) -> int:
    global truck_available_time
    global shovel_available_time
    global last_real_shovel_mass
    global real_shovel_mass
    global dump_available_time
    global last_real_dump_mass
    global real_dump_mass
    global rl_allow
    global rl_evaluate
    global is_legal

    if dispatch_method == 0 or rl_evaluate:
        if task_id == 2:  # 代表从卸载点到装载点
            if next_dest >= shovels:
                is_legal = False
                target = np.argmin((np.maximum(shovel_available_time,
                                               env.now + com_time[start_area][:]) + loading_time - env.now))
                return target
            else:
                return next_dest

        if task_id == 3:  # 代表从装载点到卸载点
            if next_dest < shovels:
                is_legal = False
                target = np.argmin(
                    (np.maximum(dump_available_time, env.now + go_time[:, start_area]) + unloading_time - env.now))
                return target
                # return np.random.randint(0, dumps, 1)[0]
            else:
                return next_dest % shovels
    else:    # dispatch_method == 1 or rl_allow = False
        if task_id == 2:    # 代表从卸载点到装载点
            return np.random.randint(0, shovels, 1)[0]

        if task_id == 3:    # 代表从装载点到卸载点
            return np.random.randint(0, dumps, 1)[0]


def walk_process(env, start_area, truck_id, next_q, direction):
    # 模拟矿卡行走的行为

    global go_to_unload_point_vehical_num
    global go_to_excavator_vehical_num

    global walking_go_to_unload_point_vehical_num
    global walking_go_to_excavator_vehical_num

    global reach_excavator_time_list
    global reach_dump_time_list

    global wating_in_excavator_vehical_num
    global wating_in_unload_point_vehical_num

    global shovel_available_time
    global dump_available_time
    global truck_available_time

    global last_real_shovel_mass
    global last_real_dump_mass

    global real_shovel_mass
    global real_dump_mass

    global truck_stage

    global truck_process

    global process_start_time

    global cost

    global truck_task

    global goto_excavator_traffic_flow_num

    global goto_dump_traffic_flow_num

    while True:
        task_id = 0
        if "go to unload_point" == direction:
            task_id = 3  # 代表从装载点到卸载点
        elif "go to excavator" == direction:
            task_id = 2  # 代表从卸载点到装载点

        # rl modify
        # 当前请求调度车辆为RL控制车辆
        global rl_truck
        if rl_truck == truck_id:
            dispatch_method = 0  # use agent policy
        else:
            dispatch_method = 1  # use heuristic policy

        # 进行卡调请求，得到目标电铲/卸载点id
        goal_area = truck_schedule_send_post(start_area, task_id, dispatch_method)

        # rl modify
        # 启发式调度动作
        global heu_action
        if dispatch_method == 1:
            if "go to unload_point" == direction:
                # print("go to unload_point")
                heu_action = goal_area + shovels
                # print(heu_action)
            elif "go to excavator" == direction:
                # print("go to excavator")
                heu_action = goal_area
                # print(heu_action)

        global heu_action_time
        heu_action_time = env.now

        # 从数据库中获取行走时长,以及装载/卸载时长
        if "go to excavator" == direction:

            # 此时goal_area代表电铲id，start_area代表卸载点id
            # 本次行走时长，除以60用于将秒换算为分钟
            # walk_time = com_time[start_area][goal_area]

            walk_time = max(1, np.random.normal(com_time[start_area][goal_area], com_time[start_area][goal_area] / 5))

            # 将该条道路的车辆个数加1
            go_to_excavator_vehical_num[start_area][goal_area] = (
                    go_to_excavator_vehical_num[start_area][goal_area] + 1
            )

            # 加入对应挖机抵达列表
            reach_excavator_time_list[goal_area].append(env.now + walk_time)

            # 运输路线车次数加1
            goto_excavator_traffic_flow_num[start_area][goal_area] += 1

            ################################### 关键状态更新 ###################################
            # 更新可用时间
            shovel_available_time[goal_area] = (
                    max(env.now + walk_time, shovel_available_time[goal_area])
                    + loading_time[goal_area]
            )
            truck_available_time[truck_id] = shovel_available_time[goal_area]

            # 产量更新
            last_real_shovel_mass = copy.deepcopy(real_shovel_mass)
            real_shovel_mass[goal_area] += payload

            # 修改卡车阶段
            truck_stage[truck_id, :] = [start_area, goal_area, 0]

            # 更新行驶油耗
            cost += (empty_power - idle_power) * walk_time / 60

            # 更新矿卡任务
            truck_task[truck_id] = 0

            ####################################################################################

        elif "go to unload_point" == direction:

            # 此时goal_area代表卸载点id，start_area代表电铲id
            # 本次行走时长，除以60用于将秒换算为分钟
            # walk_time = go_time[goal_area][start_area]
            #
            walk_time = max(1, np.random.normal(go_time[goal_area][start_area], go_time[goal_area][start_area] / 5))

            # 将该条道路的车辆个数加1
            go_to_unload_point_vehical_num[start_area][goal_area] = (
                    go_to_unload_point_vehical_num[start_area][goal_area] + 1
            )

            # 加入对应卸点抵达列表
            reach_dump_time_list[goal_area].append(env.now + walk_time)

            # 运输路线车次数加1
            goto_dump_traffic_flow_num[start_area][goal_area] += 1

            ################################### 关键状态更新 ###################################
            # 修改卡车阶段
            truck_stage[truck_id, :] = [goal_area, start_area, 3]
            # 可用时间更新
            dump_available_time[goal_area] = (
                    max(env.now + walk_time, dump_available_time[goal_area])
                    + unloading_time[goal_area]
            )
            truck_available_time[truck_id] = dump_available_time[goal_area]

            # 更新行驶油耗
            cost += (heavy_power - idle_power) * walk_time / 60

            # 更新矿卡任务
            truck_task[truck_id] = 3

            ####################################################################################

        print(
            f"{round(env.now, 2)}  - truck_id: {truck_id} - from {start_area} {direction}_{goal_area} - start moving "
        )

        # 行驶开始，统计在路上行走的车辆个数
        if "go to excavator" == direction:
            # 将该条道路正在行驶的车辆个数加1
            walking_go_to_excavator_vehical_num[start_area][goal_area] = (
                    walking_go_to_excavator_vehical_num[start_area][goal_area] + 1
            )
        elif "go to unload_point" == direction:
            walking_go_to_unload_point_vehical_num[start_area][goal_area] = (
                    walking_go_to_unload_point_vehical_num[start_area][goal_area] + 1
            )

        # 记录进程开始时间
        process_start_time[truck_id] = env.now

        # 阻塞行走时间
        global request_id
        request_id = yield env.timeout(float(walk_time), value=2)  # 行走时间,单位为分钟

        ##########################################

        # 重置任务进程
        truck_process[truck_id] = 0

        # 工作矿卡索引(stage > 0)
        work_truck_idxs = np.where(truck_stage[:, -1] >= 0)

        # 进程时间增加
        truck_process[work_truck_idxs] = truck_process[work_truck_idxs] + float(walk_time)

        ##########################################

        # 行驶结束，统计在路上行走的车辆个数
        if "go to excavator" == direction:
            # 将该条道路正在行驶的车辆个数减1
            walking_go_to_excavator_vehical_num[start_area][goal_area] = (
                    walking_go_to_excavator_vehical_num[start_area][goal_area] - 1
            )
            # 行走结束，将等待装载的车辆个数加1
            wating_in_excavator_vehical_num[goal_area] = (
                    wating_in_excavator_vehical_num[goal_area] + 1
            )

            # 行走结束，将矿卡状态修改为1
            truck_stage[truck_id, -1] = 1

            # 行走结束, 更新矿卡状态为等待
            truck_task[truck_id] = 1

            # 行走结束, 更新矿卡等待时间
            waiting_start_time[truck_id] = env.now
        elif "go to unload_point" == direction:
            walking_go_to_unload_point_vehical_num[start_area][goal_area] = (
                    walking_go_to_unload_point_vehical_num[start_area][goal_area] - 1
            )
            # 行走结束，将等待卸载的车辆个数加1
            wating_in_unload_point_vehical_num[goal_area] = (
                    wating_in_unload_point_vehical_num[goal_area] + 1
            )

            # 行走结束，将矿卡状态修改为3
            truck_stage[truck_id, -1] = 4

            # 行走结束, 更新矿卡状态为等待
            truck_task[truck_id] = 4

            # 行走结束, 更新矿卡等待时间
            waiting_start_time[truck_id] = env.now

        next_q[goal_area].put(truck_id)  # 将到来的truck放到目标队列中

        print(
            f"{round(env.now, 2)}  - truck_id: {truck_id} - {direction}_{goal_area} - end moving - walk time {walk_time}"
        )

        # env.exit()  # 该函数的作用等同于return,直接退出该函数
        return


def excavator_func(env: simpy.Environment, e_q: simpy.Store, u_q, excavator_id):
    # 模拟一个电铲, 一个电铲同时只能处理一台矿卡
    truck_source = simpy.Resource(env, capacity=1)

    global last_real_dump_mass
    global last_real_shovel_mass

    global real_dump_mass
    global real_shovel_mass

    global reach_excavator_time_list

    def process(truck_id):
        # 模拟电铲一次工作的进程
        with truck_source.request() as req:
            yield req
            print(
                f"{round(env.now, 2)}  - truck_id: {truck_id} - excavator: {excavator_id} - Begin Loading"
            )

            # 开始装载，记录装载时间
            global load_start_time
            load_start_time[excavator_id] = env.now

            # 开始装载，将等待装载的车辆个数减1
            global wating_in_excavator_vehical_num
            wating_in_excavator_vehical_num[excavator_id] = (
                    wating_in_excavator_vehical_num[excavator_id] - 1
            )

            # 开始装载，将装载车辆个数加1
            global loading_in_excavator_vehical_num
            loading_in_excavator_vehical_num[excavator_id] = (
                    loading_in_excavator_vehical_num[excavator_id] + 1
            )

            # 开始装载，将 reach list 弹出
            reach_excavator_time_list[excavator_id].pop(0)

            # 开始装载，计算装载完成时间
            global waiting_vehicle_loaded_time
            waiting_vehicle_loaded_time[excavator_id] = env.now + loading_time[excavator_id]

            global cost
            cost += (
                    (shovel_work_power[excavator_id] - shovel_idle_power[excavator_id])
                    * loading_time[excavator_id]
                    / 60
            )

            # 正在装载, 矿卡任务装载
            truck_stage[truck_id, -1] = 2

            # 电铲平均工作装载时间
            # 除以60用于将秒换算为分钟
            # load_time = loading_time[excavator_id]

            load_time = max(1, np.random.normal(loading_time[excavator_id], loading_time[excavator_id] / 5))

            # 重置任务进程
            global truck_process
            truck_process[truck_id] = 0

            # 开始装载, 更新矿卡任务
            global truck_task
            truck_task[truck_id] = 2

            # 记录服务开始时间
            global service_start_time
            service_start_time[truck_id] = env.now

            global request_id
            request_id = yield env.timeout(float(load_time), value=1)  # 进行装载操作

            # 装载结束, 更新矿卡任务
            truck_task[truck_id] = 3

            # 装载结束修改请求调度矿卡
            global request_truck
            request_truck = truck_id

            # 装载结束，记录装载时间
            global load_end_time
            load_end_time[excavator_id] = env.now

            # 工作矿卡索引(stage > 0)
            work_truck_idxs = np.where(truck_stage[:, -1] >= 0)

            # 进程时间增加
            truck_process[work_truck_idxs] = truck_process[work_truck_idxs] + float(load_time)

            # rl modify
            # 装载结束，若完成装载车辆由RL控制, 释放车辆
            global rl_truck
            if rl_truck == truck_id:
                rl_truck = -1    # 释放车辆

            # 装载结束，将装载车辆个数减1
            loading_in_excavator_vehical_num[excavator_id] = (
                    loading_in_excavator_vehical_num[excavator_id] - 1
            )

            # 装载结束，将完成装载数加1
            global excavator_loaded_vehicle_num
            excavator_loaded_vehicle_num[excavator_id] = (
                excavator_loaded_vehicle_num[excavator_id] + float(load_time)
            )

            # 装载结束，产量更新
            global real_shovel_mass
            global last_real_shovel_mass
            last_real_shovel_mass = copy.deepcopy(real_shovel_mass)
            real_shovel_mass[excavator_id] += payload

            # 记录调度矿卡位置
            truck_location[truck_id] = excavator_id

            print(
                f"{round(env.now, 2)}  - truck_id: {truck_id} - excavator: {excavator_id} - End Loading"
                " - Request Dispatching"
            )

            # 矿卡从电铲处行走到卸载点
            env.process(
                walk_process(env, excavator_id, truck_id, u_q, "go to unload_point")
            )

            # 产量统计
            if int(env.now) % 80 == 0:
                print(
                    f"Dispatching time {round(env.now, 2)} {len(real_dump_mass)} dumps masses (tonnes): {last_real_dump_mass}"
                )

    while True:
        truck_id = yield e_q.get()
        env.process(process(truck_id))


def unloadpoint_func(env: simpy.Environment, u_q: simpy.Store, e_q, unload_point_id):
    # 模拟一个卸载点, 一个卸载点同时只能处理一台矿卡
    truck_source = simpy.Resource(env, capacity=1)

    global real_dump_mass
    global real_shovel_mass
    global truck_location
    global cycle_time

    global reach_dump_time_list

    def process(truck_id):
        # 模拟卸载点一次工作的进程
        with truck_source.request() as req:
            yield req
            print(
                f"{round(env.now, 2)}  - truck_id: {truck_id} - UnloadPoint: {unload_point_id} - Begin Unloading"
            )

            # 开始卸载，记录卸载时间
            global unload_start_time
            unload_start_time[unload_point_id] = env.now

            # 开始卸载，将等待卸载的车辆个数减1
            global wating_in_unload_point_vehical_num
            wating_in_unload_point_vehical_num[unload_point_id] = (
                    wating_in_unload_point_vehical_num[unload_point_id] - 1
            )

            # 开始卸载，将正在的卸载车辆个数加1
            global unloading_in_unload_point_vehical_num
            unloading_in_unload_point_vehical_num[unload_point_id] = (
                    unloading_in_unload_point_vehical_num[unload_point_id] + 1
            )

            # 装载结束，将reach list 弹出
            reach_dump_time_list[unload_point_id].pop(0)

            # 开始卸载，计算卸载完成时间
            global waiting_vehicle_unloaded_time

            waiting_vehicle_unloaded_time[unload_point_id] = env.now + unloading_time[unload_point_id]

            # 矿卡任务装载-正在卸载
            truck_stage[truck_id, -1] = 5

            # 卸载点平均工作卸载时间
            # 除以60用于将秒换算为分钟
            # unload_time = unloading_time[unload_point_id]

            unload_time = max(1, np.random.normal(unloading_time[unload_point_id], unloading_time[unload_point_id] / 5))

            # 记录服务开始时间
            global service_start_time
            service_start_time[truck_id] = env.now

            # 开始卸载, 更新矿卡任务
            global truck_task
            truck_task[truck_id] = 4

            # 阻塞卸载时间
            global request_id
            request_id = yield env.timeout(float(unload_time), value=1)  # 进行卸载操作

            # 卸载结束, 更新矿卡任务
            truck_task[truck_id] = 0

            # 卸载结束修改请求调度矿卡
            global request_truck
            request_truck = truck_id

            # 卸载结束，记录卸载时间
            global unload_end_time
            unload_end_time[unload_point_id] = env.now

            # 重置任务进程
            global truck_process
            truck_process[truck_id] = 0

            # 工作卡车索引 (stage > 0)
            work_truck_idxs = np.where(truck_stage[:, -1] >= 0)

            # 进程时间增加
            truck_process[work_truck_idxs] = truck_process[work_truck_idxs] + float(unload_time)

            # rl modify
            # 卸载结束, 若完成卸载车辆由RL控制, 释放车辆
            global rl_truck
            if rl_truck == truck_id:
                rl_truck = -1    # 释放车辆

            # 卸载结束，将卸载车辆个数减1
            unloading_in_unload_point_vehical_num[unload_point_id] = (
                    unloading_in_unload_point_vehical_num[unload_point_id] - 1
            )

            # 卸载结束，将完成卸载数加1
            global dump_loaded_vehicle_num
            dump_loaded_vehicle_num[unload_point_id] = (
                dump_loaded_vehicle_num[unload_point_id] + float(unload_time)
            )

            # 卸载结束，产量更新
            global real_dump_mass
            global last_real_dump_mass
            last_real_dump_mass = copy.deepcopy(real_dump_mass)
            real_dump_mass[unload_point_id] += payload

            # 记录调度矿卡位置
            truck_location[truck_id] = shovels + unload_point_id

            print(
                f"{round(env.now, 2)}  - truck_id: {truck_id} - UnloadPoint: {unload_point_id} - End Unloading"
                " - Request Dispatching"
            )

            # 矿卡从卸载点处行走到电铲
            env.process(
                walk_process(env, unload_point_id, truck_id, e_q, "go to excavator")
            )

    while True:
        truck_id = yield u_q.get()
        env.process(process(truck_id))


# 在停车场按照固定时间生成一定数量的矿卡
def generate_truck_in_parking_lot(env, e_q, u_q):
    global shovel_available_time
    global dump_available_time
    global truck_available_time
    global last_real_shovel_mass
    global real_shovel_mass
    global truck_stage

    def process(truck_id, walk_time, goal_area, e_q):

        # 记录初始阶段矿卡调度，用于schedule的构造
        truck_stage[truck_id, :] = np.array([0, goal_area, 0])
        # 更新电铲，矿卡可用时间
        shovel_available_time[goal_area] = (
                max(env.now + walk_time, shovel_available_time[goal_area])
                + loading_time[goal_area]
        )
        truck_available_time[truck_id] = shovel_available_time[goal_area]

        go_to_excavator_vehical_num[0][goal_area] = (
                go_to_excavator_vehical_num[0][goal_area] + 1
        )

        # 加入对应挖机抵达列表
        reach_excavator_time_list[goal_area].append(env.now + walk_time)

        # 重置任务进程
        global truck_process
        truck_process[truck_id] = 0

        # 记录进程开始时间
        process_start_time[truck_id] = env.now

        # rl modify
        # 若当前矿卡为RL控制矿卡, 记录启动时间
        global rl_truck
        global action_time
        if rl_truck == truck_id:
            action_time = env.now

        # 阻塞行走时间
        global request_id
        request_id = yield env.timeout(float(walk_time), value=2)  # 行走时间,单位为分钟

        # 工作卡车索引 (stage > 0)
        work_truck_idxs = np.where(truck_stage[:, -1] >= 0)

        # 进程时间增加
        truck_process[work_truck_idxs] = truck_process[work_truck_idxs] + float(walk_time)

        # 产量更新
        real_shovel_mass[goal_area] += payload

        e_q[goal_area].put(truck_id)  # 将到来的truck放到电铲的队列中

        # 行走结束，将等待装载的车辆个数加1
        wating_in_excavator_vehical_num[goal_area] = (
                wating_in_excavator_vehical_num[goal_area] + 1
        )

        # 行走结束, 更新矿卡等待时间
        waiting_start_time[truck_id] = env.now

        print(
            f"{round(env.now, 2)}  - truck_id: {truck_id} - From Parking Lot to WorkArea:{goal_area} end moving "
            f"walk time {walk_time}"
        )

    for i in range(truck_num):
        # 模拟矿卡随机请求调度
        t = 1  # 固定停1*60=60秒

        # 记录进程开始时间
        process_start_time[i] = env.now

        # 阻塞行走时间
        global request_id
        request_id = yield env.timeout(t, value=2)

        global truck_process

        # 工作矿卡索引(stage > 0)
        work_truck_idxs = np.where(truck_stage[:, -1] >= 0)

        # 进程时间增加
        truck_process[work_truck_idxs] = truck_process[work_truck_idxs] + t

        task_id = 1  # task_id等于1，说明是从停车场到装载点

        target = truck_schedule_send_post_start(i, 0, task_id, env)  # 得到电铲id

        # 本次行走时长
        walk_time = com_time[0][target]

        print(
            f"{round(env.now, 2)} - truck_id: {i} - From Parking Lot to WorkArea:{target} start moving "
        )

        env.process(process(i, walk_time, target, e_q))

env = simpy.Environment()


def env_reset(rl_mode=False):
    global go_to_unload_point_vehical_num  # 用于保存每条卸载道路上经过的车辆个数
    global go_to_excavator_vehical_num  # 用于保存每条装载道路上的经过的车辆总个数

    global walking_go_to_unload_point_vehical_num  # 卸载道路上正在行走的车辆个数
    global walking_go_to_excavator_vehical_num  # 装载道路上正在行走的车辆个数

    global reach_excavator_time_list  # 驶往挖机矿卡预期抵达时间
    global reach_dump_time_list  # 驶往卸点预期抵达时间

    global loading_in_excavator_vehical_num  # 挖机装车数
    global unloading_in_unload_point_vehical_num  # 卸点卸车数

    global wating_in_excavator_vehical_num  # 挖机排队等待装载矿卡数
    global wating_in_unload_point_vehical_num  # 卸点排队等待卸载矿卡数

    global excavator_loaded_vehicle_num  # 挖机完成装载的车次数
    global dump_loaded_vehicle_num  # 卸点完成卸载的车次数

    global waiting_vehicle_loaded_time  # 完成所有排队等待车辆装载时间
    global waiting_vehicle_unloaded_time  # 完成所有排队等待车辆卸载时间

    global dump_available_time  # 卸点最近一次可用时间
    global shovel_available_time  # 挖机最近一次可用时间
    global truck_available_time  # 矿卡最近一次可用时间

    global real_shovel_mass  # 挖机实际装载量
    global real_dump_mass  # 卸点实际卸载量

    global last_real_shovel_mass  # 上一次调度任务挖机实际装载量
    global last_real_dump_mass  # 上一次调度任务卸点实际卸载量

    global truck_stage  # 标记矿卡位于哪个阶段（0：空运阶段，1：装载阶段，2：重运阶段， 3：卸载阶段）

    global cost  # 记录燃油消耗

    global recording  # 数据统计{时间(min), 产量(tonnes), 油耗(liters)}

    global process_start_time  # 矿卡执行当前行走任务的起始时间

    global service_start_time  # 矿卡执行卸载或装载的起始时间

    global waiting_start_time  # 矿卡开始等待时间

    global truck_location  # 矿卡当前位置

    global request_truck  # 当前请求调度矿卡

    global truck_process  # 矿卡当前任务持续时间

    global next_dest  # 矿卡下一目的地

    global action_time  # 调度下发时间

    global truck_waiting_from_last_act  # 车辆自上一次动作到当前动作等待时间

    global truck_task  # 车辆当前任务

    global request_id  # 调度编号

    global goto_excavator_traffic_flow_num  # 驶往挖机各运输路线实际车次
    global goto_dump_traffic_flow_num  # 驶往卸点各运输路线实际车次

    global load_start_time  # 挖机开始装载时间
    global unload_start_time  # 卸点开始卸载时间

    global load_end_time  # 挖机结束装载时间
    global unload_end_time  # 卸点结束装载时间

    global episode

    global rl_truck

    global rl_allow

    global rl_evaluate

    global heu_rpm

    global heu_action

    global heu_action_time

    global is_legal

    # 实例环境
    global env
    env = simpy.Environment()

    # 获取装载点和卸载点的个数
    num_of_load_area = shovels
    num_of_unload_area = dumps

    e_q = []
    for _ in range(num_of_load_area):
        e_q.append(simpy.Store(env))

    u_q = []
    for _ in range(num_of_unload_area):
        u_q.append(simpy.Store(env))

    # 保存每条道路的车辆个数
    go_to_unload_point_vehical_num = np.zeros((num_of_load_area, num_of_unload_area))
    go_to_excavator_vehical_num = np.zeros((num_of_unload_area, num_of_load_area))

    # real_comp_workload = np.zeros(dumps)

    # 统计在路上行驶的车辆个数
    walking_go_to_unload_point_vehical_num = np.zeros(
        (num_of_load_area, num_of_unload_area)
    )
    walking_go_to_excavator_vehical_num = np.zeros(
        (num_of_unload_area, num_of_load_area)
    )

    # 初始化车辆抵达列表
    reach_excavator_time_list = [[] for _ in range(shovels)]   # 驶往挖机矿卡预期抵达时间
    reach_dump_time_list = [[] for _ in range(dumps)]  # 驶往卸点预期抵达时间

    # 统计正在装载或者卸载的车辆个数
    loading_in_excavator_vehical_num = np.zeros(num_of_load_area)
    unloading_in_unload_point_vehical_num = np.zeros(num_of_unload_area)

    # 统计正在排队的车辆个数
    wating_in_excavator_vehical_num = np.zeros(num_of_load_area)
    wating_in_unload_point_vehical_num = np.zeros(num_of_unload_area)

    # 初始化装卸载完成车次数
    excavator_loaded_vehicle_num = np.zeros(num_of_load_area)
    dump_loaded_vehicle_num = np.zeros(num_of_unload_area)

    # 初始化完成排队车辆服务时间
    waiting_vehicle_loaded_time = np.zeros(shovels)
    waiting_vehicle_unloaded_time = np.zeros(dumps)

    # 初始化设备可用时间
    dump_available_time = np.zeros(num_of_unload_area)
    shovel_available_time = np.zeros(num_of_load_area)
    truck_available_time = np.zeros(truck_num)

    # 初始化实时产量
    last_real_shovel_mass = np.zeros(num_of_load_area)
    last_real_dump_mass = np.zeros(num_of_unload_area)

    real_shovel_mass = np.zeros(num_of_load_area)
    real_dump_mass = np.zeros(num_of_unload_area)

    # 初始化矿卡状态
    truck_stage = np.full((truck_num, 3), -1)

    # 初始化进程开始时间
    process_start_time = np.full((truck_num, 1), 0, dtype=float)

    # 初始化任务执行时间
    truck_process = np.full((truck_num, 1), 0, dtype=float)

    # 初始化服务开始时间
    service_start_time = np.full((truck_num, 1), 0, dtype=float)

    # 矿卡开始等待时间
    waiting_start_time = np.zeros(truck_num)

    # 初始化矿卡位置
    truck_location = np.full((truck_num, 1), 0, dtype=float)

    # 当前请求调度矿卡
    request_truck = 0

    # 初始化油耗
    cost = 0

    # 初始化统计表
    recording = [[0, 0, 0]]

    # 调度开始事件
    action_time = env.now

    truck_waiting_from_last_act = np.zeros(truck_num)

    # 初始化卡车当前任务类型
    truck_task = np.ones(truck_num) * -1

    # 初始化请求调度编号
    request_id = 0

    # 初始化各路线车次数
    goto_excavator_traffic_flow_num = np.zeros((dumps, shovels))
    goto_dump_traffic_flow_num = np.zeros((shovels, dumps))

    load_start_time = np.zeros((shovels, ), dtype=float)
    unload_start_time = np.zeros((dumps, ), dtype=float)

    load_end_time = np.zeros((shovels, ), dtype=float)
    unload_end_time = np.zeros((dumps, ), dtype=float)

    episode += 1

    # rl modify
    # 任意选择车辆作为初始RL控制矿卡
    rl_truck = np.random.randint(0, truck_num)

    # rl modify
    # 允许 agent 调度车辆
    rl_allow = True

    # rl modify
    # agent 测试模式
    rl_evaluate = rl_mode

    # rl modify
    heu_rpm = []

    heu_action = 0

    heu_action_time = 0

    is_legal = True

    # 启动挖机及卸点进程
    for i in range(num_of_load_area):
        env.process(excavator_func(env, e_q[i], u_q, excavator_id=i))

    for i in range(num_of_unload_area):
        env.process(unloadpoint_func(env, u_q[i], e_q, unload_point_id=i))

    # 从停车位开始向电铲派车
    env.process(generate_truck_in_parking_lot(env, e_q, u_q))

    # 信息统计进程
    # env.process(info_control_process(env))


# env.run(480)

def sim_step(action: int):
    """Go step in simulation environment given an action.

    :param action: destination for requesting truck
    :return:
        location(int),
        wating_in_excavator_vehical_num(int),
        wating_in_unload_point_vehical_num(int),
        goto_destination_time(float),
        waiting_time(float),
        env.now(float),
        reward(float),
        excavator_utilization(%),
        throughput(float)
    """
    global episode
    global rl_truck
    global request_truck
    global heu_rpm
    global heu_action
    global heu_action_time

    global reach_excavator_time_list  # 驶往挖机矿卡预期抵达时间
    global reach_dump_time_list  # 驶往卸点预期抵达时间

    global goto_excavator_traffic_flow_num
    global goto_dump_traffic_flow_num

    global waiting_vehicle_loaded_time
    global waiting_vehicle_unloaded_time

    global wating_in_excavator_vehical_num
    global wating_in_unload_point_vehical_num

    # 请求车辆调度目的地为action
    global next_dest
    next_dest = action

    # 动作时间为环境时间
    global action_time
    action_time = env.now

    # 启发式调度池
    global heu_rpm
    heu_rpm = []

    # 将请求调度车辆作为RL控制车辆
    rl_truck = request_truck

    # 当前时间正在驶往各目的地的矿卡(不含已抵达目的地矿卡)
    for dump_id in range(dumps):
        reach_dump_time_list[dump_id].sort()
        # reach_dump_time_list[dump_id] = [n for n in reach_dump_time_list[dump_id] if n > env.now]

    for excavator_id in range(shovels):
        reach_excavator_time_list[excavator_id].sort()
        # reach_excavator_time_list[excavator_id] = [n for n in reach_excavator_time_list[excavator_id] if n > env.now]

    global request_id

    print(f'rl truck {rl_truck} start moving at {env.now}')

    if rl_evaluate:

        # 矿卡等待持续请求调度, 跳过重复请求
        while abs(action_time - env.now) < 1E-6:
            env.step()

        while request_id != 1:
            env.step()

        reward = 0
    else:

        # 初始化调度记录
        heu_exp = []

        _heu_rpm_accum(heu_exp, action)

        current_action = action

        # 矿卡等待持续请求调度, 跳过重复请求
        while abs(action_time - env.now) < 1E-6:
            env.step()

        # 推进进程直到车辆请求调度, request_id = 1 行走结束, 2 请求调度
        # 保证触发的是请求调度而不是行走结束
        while request_id != 1:
            env.step()

        _heu_rpm_accum(heu_exp, current_action)

        # 调度记录加入经验池
        heu_rpm.append(heu_exp)

        # agent 控制车辆 rl_truck，期间其他车辆使用heu
        # 仿真环境step, 直到RL调度车辆为空
        while rl_truck >= 0:

            # 车辆请求调度, 推进进程为车辆下发调度目的地
            env.step()

            # 初始化调度记录
            heu_exp = []

            _heu_rpm_accum(heu_exp, heu_action)

            current_heu_action = heu_action

            # 矿卡等待持续请求调度, 跳过重复请求
            while abs(heu_action_time - env.now) < 1E-6:
                env.step()

            # 推进进程直到车辆请求调度
            while request_id != 1:
                env.step()

            # 结束调度-更新调度记录
            # print(f'calculate after at {env.now}')
            _heu_rpm_accum(heu_exp, current_heu_action)

            # 调度记录加入经验池
            heu_rpm.append(heu_exp)

        print(f'rl truck {rl_truck} end task at {env.now}')

        global is_legal
        if is_legal:
            reward = (env.now - action_time) / 30

            reward = np.exp(-reward)

            is_legal = True

        else:
            reward = -1

            is_legal = True

        # rl modify
        global rl_allow
        rl_allow = False

        jump_action_time = env.now

        # 矿卡等待持续请求调度, 跳过重复请求
        while abs(jump_action_time - env.now) < 1E-6:
            env.step()

        while request_id != 1:
            env.step()

        print(f'request_id: {request_id} - truck: {request_truck}')

        rl_allow = True

    # 更新请求调度位置
    location = int(truck_location[request_truck][0])

    goto_destination_time = _get_walking_time(location)

    waiting_time = _waiting_time_state_cal(location, env.now)

    global waiting_vehicle_loaded_time
    global waiting_vehicle_unloaded_time

    waiting_vehicle_time = np.hstack((waiting_vehicle_loaded_time, waiting_vehicle_unloaded_time))

    location_norm = location / (shovels + dumps)
    goto_destination_time_norm = goto_destination_time / 60
    waiting_time_norm = waiting_time / 60
    now_norm = env.now / T
    waiting_vehicle_time_norm = waiting_vehicle_time / T

    # TODO：应该把 loading time 和 unloading time 算在状态里

    return location_norm, waiting_vehicle_time_norm, goto_destination_time_norm, waiting_time_norm, now_norm, reward, _excavator_utilization(), _throughput_reward(), heu_rpm


def _get_artificial_reward(last_truck_location: int, action: int) -> float:
    '''
    人工奖励函数II

    车辆预期等待时间

    :param last_truck_location: 动作前调度车辆位置
    :param action: 调度指令
    :return: 奖励值
    '''
    goto_destination_time = _get_walking_time(last_truck_location)

    global request_truck

    waiting_time = _waiting_time_state_cal(last_truck_location, env.now)

    if last_truck_location < shovels:  # 位于挖机, 驶往卸载点
        if action < shovels:    # 调度目的地为挖机
            return -1
        else: # [0, 0, 1]
            destination = action
            waiting_time_to_des = waiting_time[destination]
            walk_time = goto_destination_time[destination]

            return np.exp(-(waiting_time_to_des + walk_time + unloading_time[action - shovels]) / 30)

    else:   # 位于卸载点, 驶往挖机
        if action >= shovels:    # 调度目的地为卸载点
            return -1
        else: # [1, 0, 0]
            destination = action
            waiting_time_to_des = waiting_time[destination]
            walk_time = goto_destination_time[destination]

            return np.exp(-(waiting_time_to_des + walk_time + loading_time[action]) / 30)
            # return 1


def _get_simulation_reward_utilization(location: int, action: int, last_action_time: int, now: float) -> float:
    '''
    仿真奖励函数II

    相邻动作时间内设备空闲率

    :param last_wating_in_excavator_vehical_num:
    :param last_wating_in_unload_point_vehical_num:
    :param location:
    :param action:
    :param action_time:
    :return:
    '''

    # excavator_utilization, dump_utilization = _utilization_state_cal(last_action_time, now)

    utilization = _utilization_state_cal(last_action_time, now, action)

    if location < shovels:  # 位于挖机, 驶往卸载点
        if action < shovels:    # 调度目的地为挖机
            return -1
        else: # [0, 0, 1]
            # return np.exp(dump_utilization / 1.5) - 1.0
            return np.exp(utilization / 1.5) - 1.0
    else:   # 位于卸载点, 驶往挖机
        if action >= shovels:    # 调度目的地为卸载点
            return -1
        else: # [1, 0, 0]
            # return np.exp(dump_utilization / 1.5) - 1.0
            return np.exp(utilization / 1.5) - 1.0


def _get_simulation_waiting_time(location: int, action: int, action_time: float, now: float) -> float:
    '''
    Generate trucks summation waiting time.
    :param action_time:
    :param now:
    :return:
    '''
    global truck_waiting_from_last_act
    global service_start_time
    global waiting_start_time

    for truck_id in range(truck_num):
        wait_start = waiting_start_time[truck_id]
        service_start = service_start_time[truck_id]
        if wait_start <= service_start:
            truck_waiting_from_last_act[truck_id] = max(0, (min(now, service_start) - max(wait_start, action_time)))
        else:
            truck_waiting_from_last_act[truck_id] = now - max(wait_start, action_time)

    total_waiting_time = np.sum(truck_waiting_from_last_act) / (now - action_time)

    if location < shovels:  # 位于挖机, 驶往卸载点
        if action < shovels:    # 调度目的地为挖机
            return -1
        else: # [0, 0, 1]
            return np.exp(-total_waiting_time / 10)
    else:   # 位于卸载点, 驶往挖机
        if action >= shovels:    # 调度目的地为卸载点
            return -1
        else: # [1, 0, 0]
            return np.exp(-total_waiting_time / 10)


def _get_walking_time(location: int) -> np.array(float):
    '''
    行走时间函数

    根据具体车辆位置，计算驶往各目的地的行驶时间
    :param location: 调度车辆位置
    :return: 驶往各目的地时间
    '''
    goto_destination_time = np.zeros(shovels + dumps)

    if location < shovels:  # 位于挖机
        goto_destination_time[0:shovels] = 0  # 驶往挖机无效
        goto_destination_time[shovels:] = go_time[:, location].flatten()
    else:  # 位于卸点
        # com_time[location % shovels, :].flatten()
        goto_destination_time[0:shovels] = com_time[location - shovels, :].flatten()
        goto_destination_time[shovels:] = 0  # 驶往卸点无效

    return goto_destination_time


def _throughput_reward() -> float:
    '''
    :return: 上状态观测时间点到当前状态观测时间点的产量变化
    '''
    # return np.sum(real_dump_mass - last_real_dump_mass)
    return np.sum(real_dump_mass)


def _process_state(env):
    '''
    计算各矿卡任务进程
    :param env: 仿真环境
    :return: 矿卡任务进程
    '''
    global process_start_time
    global truck_process
    for truck_id in range(truck_num):
        truck_process[truck_id] = env.now - process_start_time[truck_id]

    return truck_process


def _waiting_time_state_cal(location, now):
    global reach_excavator_time_list
    global reach_dump_time_list
    global waiting_vehicle_unloaded_time
    global waiting_vehicle_loaded_time

    waiting_time = np.zeros(shovels + dumps)

    if location < shovels:  # 位于挖机
        for dump_id in range(dumps):
            waiting_time[shovels + dump_id] = _waiting_time_cal(location, dump_id, now)
    else:  # 位于卸点
        for shovel_id in range(shovels):
            waiting_time[shovel_id] = _waiting_time_cal(location, shovel_id, now)

    return waiting_time


def _waiting_time_cal(location, destination, now):
    """
    Generate request truck waiting time.
    :param location: request truck location
    :param destination: request truck destination
    :param now: simulation current.
    :return:
    """
    global reach_dump_time_list
    global reach_excavator_time_list
    global waiting_vehicle_unloaded_time
    global waiting_vehicle_loaded_time
    global request_truck

    reach_excavator_bf_list = [[] for _ in range(shovels)]
    reach_dump_bf_list = [[] for _ in range(dumps)]
    if location < shovels:  # 位于挖机
        # 驶往指定目的地时间
        goto_destination_time = _get_walking_time(location)[destination + shovels]
        # 当前车辆驶往指定目的地抵达时间
        request_truck_reach_time = now + goto_destination_time
        # 初始化等待时间为完成等待车辆服务
        waiting_time = waiting_vehicle_unloaded_time[destination]
        # 在当前车辆前抵达目的地的车辆序列
        reach_dump_bf_list = [n for n in reach_dump_time_list[destination] if (request_truck_reach_time > n)]
        reach_dump_bf_list.sort()

        for r in reach_dump_bf_list:
            # 当前车辆卸载时间
            waiting_time = max(waiting_time, r) + unloading_time[destination]

        return max(waiting_time - request_truck_reach_time, 0)
    elif location >= shovels:  # 位于卸点
        # 驶往指定目的地时间
        goto_destination_time = _get_walking_time(location)[destination]
        # 当前车辆驶往指定目的地抵达时间
        request_truck_reach_time = now + goto_destination_time
        # 初始化等待时间为完成等待车辆服务
        waiting_time = waiting_vehicle_loaded_time[destination]
        # 在当前车辆前抵达目的地的车辆序列
        reach_excavator_bf_list = [n for n in reach_excavator_time_list[destination] if
                                   (request_truck_reach_time > n)]
        reach_excavator_bf_list.sort()

        for r in reach_excavator_bf_list:
            # 当前车辆等待时间
            waiting_time = max(waiting_time, r) + loading_time[destination]

        return max(waiting_time - request_truck_reach_time, 0)


def _utilization_state_cal(last_action_time, now, action):
    '''
    计算设备利用率
    :param last_action_time: 上一动作时间
    :param now: 当前时间
    :return: 挖机和卸点设备利用率
    '''

    global load_start_time
    global load_end_time
    global unload_start_time
    global unload_end_time

    excavator_working_time = 0
    dump_working_time = 0

    time_period = now - last_action_time

    # excavator_id = 0
    # unload_point_id = shovels

    if action < shovels:
        excavator_id = action

        start = load_start_time[excavator_id]
        end = load_end_time[excavator_id]
        if end <= start:
            end = now
        if action_time > end:
            excavator_working_time += 0
        else:
            excavator_working_time += (end - max(last_action_time, start))

        return excavator_working_time / time_period
    else:
        unload_point_id = action - shovels

        start = unload_start_time[unload_point_id]
        end = unload_end_time[unload_point_id]
        if end <= start:
            end = now
        if action_time > end:
            dump_working_time += 0
        else:
            dump_working_time += (end - max(last_action_time, start))

        return dump_working_time / time_period


def _excavator_utilization():
    """
    计算一个班次内铲车利用率
    :return: 平均铲车利用率
    """
    global excavator_loaded_vehicle_num

    return np.sum(excavator_loaded_vehicle_num) / len(excavator_loaded_vehicle_num)


def _heu_rpm_accum(heu_exp, heu_action):
    """将启发式调度记录投入经验池
    :param heu_exp: (List) 一条启发式调度经验
    :param heu_action: (int) 调度动作
    :return:
    """
    global heu_rpm
    global request_truck
    global truck_location
    global waiting_vehicle_loaded_time
    global waiting_vehicle_unloaded_time

    location = int(truck_location[request_truck][0])

    goto_destination_time = _get_walking_time(location)

    waiting_time = _waiting_time_state_cal(location, env.now)

    waiting_vehicle_time = np.hstack((waiting_vehicle_loaded_time, waiting_vehicle_unloaded_time))

    location_norm = location / (shovels + dumps)
    goto_destination_time_norm = goto_destination_time / 60
    waiting_time_norm = waiting_time / 60
    now_norm = env.now / T
    waiting_vehicle_time_norm = waiting_vehicle_time / T

    if len(heu_exp) == 0:
        # 正常奖励
        reward = _get_artificial_reward(location, heu_action)
        # 包含随机扰动的奖励
        heu_exp.append(np.r_[location_norm, com_time.flatten() / 60, waiting_vehicle_time_norm, goto_destination_time_norm, waiting_time_norm, now_norm])
        heu_exp.append((heu_action, 1))
        heu_exp.append(reward)
    else:
        heu_exp.append(np.r_[location_norm, com_time.flatten() / 60, waiting_vehicle_time_norm, goto_destination_time_norm, waiting_time_norm, now_norm])
        heu_exp.append(env.now >= T)

