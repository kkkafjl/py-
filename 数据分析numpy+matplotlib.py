import numpy
import matplotlib.pyplot

matplotlib.pyplot.rcParams['font.sans-serif'] = ['SimHei']  # 用来设置字体样式以正常显示中文标签
matplotlib.pyplot.rcParams['axes.unicode_minus'] = False  # 默认是使用Unicode负号，设置正常显示字符，如正常显示负号

arr_stu_info_orig = numpy.loadtxt(fname='学生信息表.txt',
                                  delimiter=',',
                                  encoding='utf-8',
                                  dtype=str)
arr_stu_score_orig = numpy.loadtxt(fname='学生成绩表.txt',
                                   delimiter=',',
                                   encoding='utf-8',
                                   dtype=str)
arr_class_info_orig = numpy.loadtxt(fname='班级信息表.txt',
                                    delimiter=',',
                                    encoding='utf-8',
                                    dtype=str)
arr_sch_info_orig = numpy.loadtxt(fname='院系信息表.txt',
                                  delimiter=',',
                                  encoding='utf-8',
                                  dtype=str)
print(arr_stu_info_orig.shape)
print(arr_stu_info_orig[:5, :])

print(arr_stu_score_orig.shape)
print(arr_stu_score_orig[:5, :])

print(arr_class_info_orig.shape)
print(arr_class_info_orig[:5, :])

print(arr_sch_info_orig.shape)
print(arr_sch_info_orig[:5, :])

arr_after_stu_info = numpy.unique(arr_stu_info_orig, axis=1)
arr_after_sch_info = numpy.unique(arr_sch_info_orig, axis=1)

numpy.savetxt(fname='去重学生信息表.csv',
              X=arr_after_stu_info,
              delimiter=' ',
              fmt='%s',
              encoding='utf-8')
numpy.savetxt(fname='去重院系信息表.csv',
              X=arr_after_sch_info,
              delimiter=' ',
              fmt='%s',
              encoding='utf-8')
arr_after_sch_score = numpy.char.strip(arr_stu_score_orig)
numpy.savetxt(fname='去除学生成绩表中存在的空白字符.csv',
              X=arr_after_sch_score,
              delimiter=' ',
              fmt='%s',
              encoding='utf-8')
numpy.savetxt(fname='学生基本信息表.csv',
              X=arr_after_sch_score[:, :3],
              delimiter=' ',
              fmt='%s',
              encoding='utf-8')
numpy.savetxt(fname='学号成绩表.csv',
              X=arr_after_sch_score.take(indices=[0, -1], axis=1),
              delimiter=' ',
              fmt='%s',
              encoding='utf-8')
numpy.savetxt(fname='学生基本信息表2.csv',
              X=arr_after_stu_info.take(indices=[2, 1, 3, 4], axis=1),
              delimiter=' ',
              fmt='%s',
              encoding='utf-8')
numpy.savetxt(fname='入学日期表.csv',
              X=arr_after_stu_info.take(indices=[2, 0], axis=1),
              delimiter=' ',
              fmt='%s',
              encoding='utf-8')
get_num_score_max = numpy.argmax(arr_stu_score_orig[1:, -1])
print(f"入学最高分对应学生信息:{arr_stu_score_orig[get_num_score_max + 1]}")
count_gril_boy = {}
for char in arr_after_stu_info[1:, -2]:
    if char in count_gril_boy.keys():
        count_gril_boy[char] += 1
    else:
        count_gril_boy[char] = 1
list_name = [str(k) for k in count_gril_boy.keys()]

list_count_gril_boy = list({k: v / sum(count_gril_boy.values())
                            for k, v in count_gril_boy.items()}.values())

matplotlib.pyplot.pie(list_count_gril_boy, labels=list_name)
matplotlib.pyplot.title("2017年入学男女生比例")
matplotlib.pyplot.savefig("2017年入学男女生比例.png")
matplotlib.pyplot.show()
