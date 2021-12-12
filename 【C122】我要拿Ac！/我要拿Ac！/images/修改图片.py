from PIL import Image

#pic = ('alien.png', 'time limit exceeded.png', 'wrong answer.png', 'runtime error.png')
#pic = ('compile error.png', 'bug.png')
#pic = ('presentation error.png', 'memory limit exceeded.png')
p = 'trap.png'
im = Image.open(p)
w, h = im.size
im.thumbnail((w/1.02, h/1.02))
im.save(p, 'png')


#image = Image.open('skeleton_2l.png')
 
# 调整图片大小，并保持比例不变
# 给定一个基本宽度
#base_width = 150
 
# 基本宽度与原图宽度的比例
#w_percent = base_width / float(image.size[0])
 
# 计算比例不变的条件下新图的长度
#h_size = int(float(image.size[1]) * float(w_percent))
 
# 重新设置大小
# 默认情况下，PIL使用Image.NEAREST过滤器进行大小调整，从而获得良好的性能，但质量很差。
#image = image.resize((base_width, h_size), Image.ANTIALIAS)
#image.save('skeleton_2l.png', 'png')
