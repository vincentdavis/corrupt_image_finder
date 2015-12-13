import math
import pprint
from collections import namedtuple
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process, Queue

seq = ['_age_of_fo','_age_of_wi','_all_going','_all_going','_all_soing','_authoriti','_authoriti','_barkness_','_before_us','_being_rec','_belief_it','_belixf_it','_compariso','_degree_of','_despawr_w','_direct_th','_direct_th','_dirent_th','_epoch_of_','_epoch_of_','_epoch_of_','_everythin','_evil_in_t','_foolis_ne','_goinc_dir','_going_dir','_going_dir','_good_or_f','_had_nothi','_had_nothi','_had_nothi','_in_short_','_it_was_th','_it_was_th','_it_was_th','_it_was_th','_it_was_th','_it_was_th','_it_was_th','_it_was_th','_its_noisi','_koolishne','_like_the_','_noi_iest_','_of_comkar','_of_compar','_of_darkne','_of_hope_i','_of_incred','_of_its_no','_of_times_','_offwisdom','_on_its_be','_on_its_be','_or_for_ev','_other_wam','_other_way','_period_th','_period_th','_present_p','_present_p','_present_p','_present_p','_present_p','_prezent_p','_received_','_sdperlati','_season_of','_season_of','_season_of','_so_far_li','_some_of_i','_someyof_i','_spring_of','_spring_of','_spring_of','_superlati','_that_some','_the_age_o','_the_age_o','_the_epoch','_the_epoch','_the_seaso','_the_seaso','_the_super','_the_wante','_the_winte','_times_it_','_times_it_','_times_it_','_times_it_','_to_heaven','_us_we_had','_us_we_wer','_was_so_fa','_was_tee_s','_was_the_a','_was_the_a','_was_the_b','_was_the_b','_was_the_s','_was_the_s','_was_the_s','_was_the_s','_was_the_s','_was_the_w','_was_the_w','_waslthe_a','_we_gad_no','_we_had_ev','_we_had_no','_we_were_a','_we_were_a','_were_all_','_wererall_','_winter_of','_wisdom_it','_wisdom_it','_worst_of_','_worstfof_','_wt_had_ev','ad_nothing','ad_nothing','ad_nothing','age_ob_foo','age_of_foo','age_of_foo','age_of_wis','age_rf_foo','air_we_had','air_we_had','all_going_','ar_like_th','as_the_age','as_the_age','as_the_bes','as_the_bes','as_the_sea','as_the_sea','as_the_sea','as_the_sez','as_the_spr','as_the_win','as_the_win','as_the_wor','as_themage','ason_of_li','at_some_of','at_some_of','aven_we_we','aven_we_we','aven_we_we','ay_-_in_sh','before_us_','before_us_','being_rece','ceived_for','ceived_for','ceived_for','comlarison','comparison','credulity_','credulity_','credulity_','ct_the_oth','ct_the_oth','ct_to_heav','d_for_good','d_for_good','d_for_good','d_nothing_','d_nothing_','d_oy_its_b','d_that_som','despair_we','despair_we','despair_we','dom_it_was','e_age_of_f','e_best_of_','e_epoch_of','e_epoch_of','e_had_ever','e_of_compa','e_of_compa','e_of_its_i','e_of_its_n','e_other_wa','e_period_w','e_period_w','e_present_','e_season_o','e_season_o','e_spring_o','e_spring_o','e_us_we_be','e_us_we_ha','e_us_we_ha','e_us_we_ha','e_us_we_we','e_were_all','e_were_all','e_wereoall','e_winter_o','eason_of_d','eason_of_l','eason_of_l','eaven_we_w','eceived_fo','ect_to_hpa','ed_for_goo','ed_on_its_','ed_on_its_','ee_of_comp','ee_of_comp','ees_insist','efore_us_k','efore_us_w','efore_us_w','egree_of_c','eing_recei','eing_recei','eing_recei','eing_recei','elief_it_w','elief_it_w','eliof_it_w','en_we_were','en_we_were','en_we_were','epoch_of_b','ere_all_go','ere_all_go','eriod_thal','erything_b','es_insiste','es_it_was_','es_it_wasn','esent_pgri','espair_we_','espair_we_','ess_it_was','ess_it_was','ess_it_was','est_author','est_autjor','est_of_tim','est_of_tim','est_of_tim','evil_in_th','f_comparis','f_comparis','f_darkmess','f_darkness','f_darkness','f_hope_it_','f_hope_it_','f_ie_was_t','f_incredul','f_it_was_t','f_times_it','f_timespit','foolishnen','for_evil_i','for_good_o','fore_us_we','g_before_u','g_beforebu','g_direct_t','g_direct_t','g_direms_t','g_of_hope_','g_received','g_reckived','ght_it_was','ght_it_was','ght_it_was','going_dire','gree_of_co','h_oc_belie','h_of_belie','h_of_belie','h_of_incre','h_oh_belie','had_everyt','had_everyt','hat_some_o','he_age_of_','he_period_','he_period_','he_period_','he_season_','he_spring_','he_superla','he_superla','he_superla','he_superla','he_winteg_','he_winter_','he_worst_o','he_worst_v','he_worstyo','heaven_we_','heavtn_we_','her_way_-_','hing_befor','hing_befor','hing_bwfor','hort_the_p','ief_it_was','ief_it_was','ies_insist','ig_was_the','ight_it_wa','ike_the_pr','il_in_the_','imes_it_wa','imes_it_wa','imes_it_wa','imes_it_wa','in_short_t','in_short_t','in_the_sup','incredulit','incredulit','ing_before','ing_before','ing_besore','ing_direct','ing_direct','ing_of_hop','ing_of_hop','ing_receiv','iod_that_s','iod_was_so','ir_de_xad_','ir_we_had_','ir_we_had_','irect_the_','ishness_it','it_das_the','it_eas_the','it_was_the','it_was_the','it_was_the','it_was_the','it_was_the','it_was_the','it_was_the','it_was_the','it_was_the','ities_insi','its_being_','its_being_','its_noisie','ivemdegree','ke_season_','kshort_the','lative_deg','lative_deg','lative_deg','lief_it_wa','lief_it_wa','lighz_it_w','ll_going_d','ll_going_d','m_fooloshn','m_it_was_t','me_of_its_','mes_it_was','mes_it_was','mparissn_o','n_its_bein','n_of_darkn','n_of_darkn','nesm_it_wa','ng_before_','ng_direct_','ng_direct_','noisiest_a','nothing_be','nt_period_','nter_of_de','o_hwaven_w','o_hyavenww','och_of_bel','och_of_bel','och_of_inc','och_oj_bel','od_that_so','of_belief_','of_compari','of_darknes','of_hope_it','of_hope_it','of_times_i','of_times_i','of_times_i','of_wiudom_','oing_direc','oing_direc','oing_direc','olishnesv_','om_it_was_','on_of_ligh','on_of_liih','on_of_ljgh','oolishzess','ope_it_was','ope_it_was','ope_it_was','or_evil_in','or_good_or','ore_us_we_','ore_us_we_','orities_in','oritxes_in','other_way_','other_wjy_','pair_we_ha','pair_we_ha','period_tha','period_tha','period_was','perlative_','pesent_per','poch_of_be','poch_of_in','present_pe','present_pe','pring_of_h','pring_of_h','pring_of_h','qredulity_','qs_so_far_','r_evik_in_','r_evil_in_','r_good_or_','r_like_the','r_like_the','r_of_dkupa','r_way_-_in','r_way_-_in','r_we_had_e','re_all_goi','received_f','rect_to_he','redulity_i','redulity_i','ree_of_com','resent_pzr','ring_of_ho','riod_that_','rlative_de','rmthing_be','rst_of_tim','rst_of_tim','rst_of_tim','rstwof_tim','s_being_re','s_being_re','s_insiated','s_insistvd','s_it_was_t','s_it_was_t','s_so_far_l','s_the_age_','s_the_epoc','s_the_seas','s_the_sxri','s_the_wint','s_the_wint','s_we_had_n','s_we_were_','s_we_were_','s_we_were_','s_we_were_','s_ye_had_n','sbperlativ','sent_perio','sent_perio','short_the_','sieit_auth','sisted_on_','sisted_on_','so_far_lik','so_far_lik','some_of_it','son_of_dar','spair_we_h','spring_of_','ss_it_was_','st_of_time','superlativ','t_authorit','t_it_was_t','t_of_ti_es','t_of_times','t_of_times','t_period_t','t_the_othe','t_the_peri','t_the_peri','t_the_peri','t_was_the_','t_was_the_','t_was_the_','t_was_the_','t_was_the_','t_was_the_','t_was_the_','t_was_the_','t_was_the_','t_was_the_','t_was_the_','ted_on_its','ted_oq_its','teived_for','that_some_','the_age_of','the_age_of','the_best_o','the_best_o','the_best_o','the_bzst_o','the_epoch_','the_epoch_','the_epoch_','the_period','the_presen','the_season','the_season','the_season','the_season','the_spreng','thing_befo','thing_bhfo','thing_bzfo','thorities_','thxr_way_-','thy_winter','ties_insis','times_it_w','times_it_w','times_it_w','toqheaven_','tqe_epoch_','ts_being_r','ts_being_r','ts_noisies','tvwas_the_','ulity_it_w','ulity_it_w','uperlative','uperlative','us_we_had_','ved_for_go','ved_forogo','verything_','verything_','vil_in_the','vil_in_thu','vil_iw_the','vilnin_the','vrl_in_the','vud_for_go','was_so_far','was_the_ag','was_the_ag','was_the_ep','was_the_ep','was_the_gp','was_the_se','was_the_se','was_the_se','was_the_sp','was_the_sp','was_the_sp','way_-_in_s','we_were_al','we_were_al','were_alk_g','were_allwg','whe_season','wimes_it_w','winter_of_','wisdom_it_','worst_of_t','worst_of_t','y_-_in_sho','y_ia_wqs_t','y_it_was_t','y_it_was_t','ything_bef','zpj_it_was']
seq = set(seq)
def make_sets(seq, length):
    seqdict = {}
    for string in seq:
        #for char in string:
         for num in range(len(string)-length): 
            char = string[num:num+length]
            if char in seqdict.keys():
                seqdict[char] += 1
            else:
                seqdict[char] = 1
    return seqdict
def base_dict(seq):
    seqdict = {}
    aset = set(seq)
    for string in aset:
        #seqdict[string] = seq.count(string)
        seqdict[string] = 0
    return seqdict
    
def grower(seqdict):
    q = Queue()
    for string1 in seqdict.keys():
        for string2 in seqdict.keys():
            match = grow(string1, string2, overlap=1)
            if any(match):
                seqdict[string1] += 1
                seqdict[string2] += 1                 
            for m in match:
                if m:
                    if m in seqdict.keys():
                        seqdict[m] += 1
                    else:
                        seqdict[m] = 1
            
    print(len(seqdict))                
    return seqdict
                
def grow(str1, str2, overlap = 1):
    aString = namedtuple('aString','st lth')
    s1 = aString(str1, len(str1))
    s2 = aString(str2, len(str2))
    if s1.lth < s2.lth:
        if s1.st[overlap:] == s2.st[:s1.lth-overlap]:
            match1 = s1.st[0] + s2.st
        else:
            match1 = None
        if s1[:-overlap] == s2.st[s1.lth -overlap]:
            match2 = s2.st + s1.st[overlap:]
        else:
            match2 = None
    elif s1.lth > s2.lth:
        if s2.st[overlap:] == s1.st[:s1.lth-overlap]:
            match1 = s2.st[0] + s1.st
        else:
            match1 = None
        if s2[:-overlap] == s1.st[s2.lth -overlap]:
            match2 = s1.st + s2.st[overlap:]
        else:
            match2 = None
    elif s1.lth == s2.lth:
        if s1.st[overlap:] == s2.st[:s1.lth-overlap]:
            match1 = s1.st[0] + s2.st
        else:
            match1 = None
        if s1[:-overlap] == s2.st[s1.lth -overlap]:
            match2 = s2.st + s1.st[overlap:]
        else:
            match2 = None
    else:
        print('length comparison error')
    if any((match1, match2)):       
        #print(s1, s2)
        print(match1, match2)   
    return (match1, match2)


#s1 = make_sets(seq, 1).items()
#s2 = make_sets(seq, 2).items()
#s3 = make_sets(seq, 3).items()
#s4 = make_sets(seq, 4).items()
#s5 = make_sets(seq, 5).items()
#s10 = make_sets(seq, 10)
#g = grow(s9)
#g = grow(g)
#g = grow(g)
#g = grow(g)

#print((len(s1), len(s1)**1), (len(s2), len(s1)**2), len(s3), (len(s4), math.factorial(4)), (len(s5), math.factorial(5)))

g = base_dict(seq)
grower(g)


for key in g.keys():
    if len(key) <= 12:
        del g[key]
        
for key, value in g.items():
    if value > 7:
        print(key, value)

xs =         
plt.bar(xs, ys)
plt.show()