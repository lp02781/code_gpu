% Kalman filter example
clear all;
dt =0.5; %sampling time
A =[1 dt ; 0 1]; %transition matrix
B =[dt^2/2; dt ];%input vector
H=[1 0]; % measurement vector
measure_noise = 10
accel_noise = 0.2; % acceleration noise (meter/sec^)
Q=accel_noise^2*[dt^4/4 dt^3/2; dt^3/2 dt^2 ]; % BBtranspose Covariance of error vector
R=measure_noise^2; % YYtranspose Covariance of noise
P=Q; % Covariance estimate
duration=100;
x_init =[0.1;0];
x_hat_init =[0.1;0];
x(:,1)= x_init;
x(:,2)=x(:,1);
x_hat(:,1)= x_hat_init;
y(1)=0;
time(1)=0;

for k=2:duration/dt
    ProcessNoise = 2*accel_noise*[dt^2/2*randn ; dt*randn];
    MeasNoise = measure_noise*randn;
    time(k)= dt*(k-1);
    u0=15;
    u(k)=u0*sin(2*pi*5*k/duration);
    x(:,k+1)=A*x(:,k)+B*u(k)+ ProcessNoise;
    y(k+1)=H*x(:,k)+ MeasNoise;
    x_hat(:,k)=A*x_hat(:,k-1)+B*u(k);
    P=A*P*A'+Q;
    S=H*P*H'+R;
    K=P*H'*inv(S);
    v=y(k+1)-H*x_hat(:,k);
    x_hat(:,k+1)=x_hat(:,k)+K*v;
    P=(1-K*H)*P;
end
time(duration/dt+1)=duration;
subplot(2,1,1),
plot(time,x(1,:),time,x_hat(1,:))
subplot(2,1,2),
plot(time,x(2,:),time,x_hat(2,:))

