import lcd
import time

lcd.init()

lcd.clear(lcd.BLUE)
lcd.rotation(0)

# 定义矩阵的行列数
rows = 3
cols = 3

# 计算每个数字的起始位置
x_start = 30  # 矩阵左上角x坐标
y_start = 30  # 矩阵左上角y坐标
cell_width = 40  # 每个单元格宽度
cell_height = 40  # 每个单元格高度

for row in range(rows):
    for col in range(cols):
        # 计算当前数字(1-9)
        num = row * cols + col + 1
        # 计算当前位置
        x = x_start + col * cell_width
        y = y_start + row * cell_height
        # 绘制数字
        lcd.draw_string(x, y, str(num), lcd.WHITE, lcd.BLUE)

time.sleep(1)
