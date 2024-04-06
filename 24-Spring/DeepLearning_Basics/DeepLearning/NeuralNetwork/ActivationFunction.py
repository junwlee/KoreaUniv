import plotly.graph_objects as go
import numpy as np

# 함수 정의
def step_func(x):
    return np.array(x > 0, dtype=np.int64)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def ReLU(x):
    return np.maximum(0, x)

# x 값 범위 설정
x = np.arange(-5.0, 5.0, 0.1)

# 각 함수의 y 값 계산
y_step = step_func(x)
y_sigmoid = sigmoid(x)
y_ReLU = ReLU(x)

# Plot 생성
fig = go.Figure()

# 계단 함수 추가
fig.add_trace(go.Scatter(x=x, y=y_step, mode='lines', name='계단 함수',
                         line=dict(color='blue', dash='dot')))

# 시그모이드 함수 추가
fig.add_trace(go.Scatter(x=x, y=y_sigmoid, mode='lines', name='시그모이드 함수',
                         line=dict(color='red')))

# ReLU 함수 추가
fig.add_trace(go.Scatter(x=x, y=y_ReLU, mode='lines', name='ReLU 함수',
                         line=dict(color='green')))

# 그래프 제목 및 축 라벨 설정
fig.update_layout(title='다양한 활성화 함수 비교',
                  xaxis_title='X',
                  yaxis_title='Y')

# 그래프 표시
fig.show()
