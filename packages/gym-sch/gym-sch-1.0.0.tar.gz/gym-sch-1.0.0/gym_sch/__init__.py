

from gym.envs.registration import register

register(
		id='sch-v6',
		entry_point='gym_sch.envs:TruckScheduleEnv',
)