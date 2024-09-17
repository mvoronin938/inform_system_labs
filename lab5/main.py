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

    def avg_time_recov_Tb_list(self, distribution) -> list:
        avg_time_recov_Tb = list()
        for i in range(distribution):
            avg_time_recov_Tb.append(random.uniform(self.avg_time_recov_Tb[0], self.avg_time_recov_Tb[1]))
        return avg_time_recov_Tb

    def actual_duration_tpi_list(self, distribution) -> list:
        actual_duration_tpi = list()
        for i in range(distribution):
            actual_duration_tpi.append(random.uniform(self.actual_duration_tpi[0], self.actual_duration_tpi[1]))
        return actual_duration_tpi


config = Config()


def trouble_free_probability(num_refuse_Q, num_exp_N):
    return 1 - (num_refuse_Q / num_exp_N)


def avg_time_estimate(cur_time_recov_Tb_dop, avg_time_recov_Tb):
    return 1 if avg_time_recov_Tb <= cur_time_recov_Tb_dop else (cur_time_recov_Tb_dop / avg_time_recov_Tb)


def avg_time_recovering(num_exp_n, avg_time_recov_tb):
    return (1 / num_exp_n) * sum(avg_time_recov_tb)

avg_time_recovering_val = avg_time_recovering(config.NUM_EXP_N, config.avg_time_recov_Tb_list(config.NUM_EXP_N))

def duration_estimate(valid_time_trip_dop, actual_duration_tpi):
    return 1 if actual_duration_tpi <= valid_time_trip_dop else (valid_time_trip_dop / actual_duration_tpi)

def avg_time_trans(num_exp_n, actual_duration_tpi):
    return (1 / num_exp_n) * sum(actual_duration_tpi)

avg_time_trans_val = avg_time_trans(config.NUM_EXP_N, config.actual_duration_tpi_list(config.NUM_EXP_N))

print(f'''
P(Y) trouble_free_probability: {trouble_free_probability(config.NUM_REFUSE_Q, config.NUM_EXP_N)}

Qв avg_time_estimate: {avg_time_estimate(config.CUR_TIME_RECOV_TB_DOP, avg_time_recovering_val)}
Tв avg_time_recovering: {avg_time_recovering_val}

Qпi duration_estimate: {duration_estimate(config.VALID_TIME_TPI_DOP,avg_time_trans_val )}
Tпi avg_time_trans_val: {avg_time_trans_val}
'''
)
