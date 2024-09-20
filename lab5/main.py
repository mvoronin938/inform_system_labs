import os
import random



class Config:
    NUM_REFUSE_Q = float(os.environ['NUM_REFUSE_Q'])
    NUM_EXP_N = int(os.environ['NUM_EXP_N'])

    AVG_TIME_RECOV_TB = os.environ['AVG_TIME_RECOV_TB'].split(',')
    CUR_TIME_RECOV_TB_DOP = float(os.environ['CUR_TIME_RECOV_TB_DOP'])

    ACTUAL_DURATION_TPI = os.environ['ACTUAL_DURATION_TPI'].split(',')
    VALID_TIME_TPI_DOP = float(os.environ['VALID_TIME_TPI_DOP'])

    BASIC_PRINC_REL = float(os.environ['BASIC_PRINC_REL'])

    @property
    def avg_time_recov_Tb(self) -> list:
        return [float(_) for _ in self.AVG_TIME_RECOV_TB]

    @property
    def actual_duration_tpi(self) -> list:
        return [float(_) for _ in self.ACTUAL_DURATION_TPI]

    @property
    def avg_time_recov_Tb_list(self):
        avg_time_recov_Tb = list()
        for i in range(self.NUM_EXP_N):
            avg_time_recov_Tb.append(random.uniform(self.avg_time_recov_Tb[0], self.avg_time_recov_Tb[1]))
        return avg_time_recov_Tb

    @property
    def actual_duration_tpi_list(self) -> list:
        actual_duration_tpi = list()
        for i in range(self.NUM_EXP_N):
            actual_duration_tpi.append(random.uniform(self.actual_duration_tpi[0], self.actual_duration_tpi[1]))
        return actual_duration_tpi


config = Config()

trouble_free_probability = 1 - (config.NUM_REFUSE_Q / config.NUM_EXP_N)

avg_time_recovering = (1 / config.NUM_EXP_N) * sum(config.avg_time_recov_Tb_list)

avg_time_estimate = 1 if avg_time_recovering <= config.CUR_TIME_RECOV_TB_DOP \
    else (config.CUR_TIME_RECOV_TB_DOP / avg_time_recovering)

avg_time_trans = (1 / config.NUM_EXP_N) * sum(config.actual_duration_tpi_list)

duration_estimate = 1 if avg_time_trans <= config.VALID_TIME_TPI_DOP \
    else (config.VALID_TIME_TPI_DOP / avg_time_trans)

final_estimate = (avg_time_estimate + duration_estimate) / 2

absolute_criteria = (final_estimate + trouble_free_probability) / 2 

related_factor = absolute_criteria / config.BASIC_PRINC_REL

related_factor_arr = [related_factor]

related_factor = sum(related_factor_arr) / len(related_factor_arr)

print(f'''
P(Y) trouble_free_probability: {trouble_free_probability}

Qв avg_time_estimate: {avg_time_estimate}
Tв avg_time_recovering: {avg_time_recovering}

Qпi duration_estimate: {duration_estimate}
Tпi avg_time_trans_val: {avg_time_trans}

Pjkm final_estimate_val: {final_estimate}

Pji absolute_criteria: {absolute_criteria}
'''
      )
