clc;

clear all;


vb = 2; % Volts
r = 10; % Ohms
l = 10e-3; % Henries
c = 4.7e-9; % Farads
dt = 1e-6; % Second

i1_initial = 0;
vc_initial = 0;
n_iterations = 500;

R_overdamped = 33e3;
R_critical = 3.3e3;
R_underdamped = 330;

[time1, i1, vl, V_overdamped] = simulate_rlc(vb, R_overdamped, l, c, dt, i1_initial, vc_initial, n_iterations);
[time1, i1, vl, V_critical] = simulate_rlc(vb, R_critical, l, c, dt, i1_initial, vc_initial, n_iterations);
[time1, i1, vl, V_underdamped] = simulate_rlc(vb, R_underdamped, l, c, dt, i1_initial, vc_initial, n_iterations);

figure;
title('Voltage Response of Series RLC Circuit');
subtitle('By Nariman Ziaie | Student ID: 40010140119030');
hold on;
plot(time1, V_overdamped, 'b');
hold on;
plot(time1, V_critical, 'g');
hold on;
plot(time1, V_underdamped, 'r');

xlabel('Time (s)');
ylabel('Voltage (V)');
legend('Overdamped','Critically damped','Underdamped');

grid on;
hold off;

function [time1, i1, vl, vc] = simulate_rlc(vb, r, l, c, dt, i1_initial, vc_initial, n_iterations)
    time1 = zeros(n_iterations + 1, 1);
    i1 = zeros(n_iterations + 1, 1);
    vl = zeros(n_iterations + 1, 1);
    vc = zeros(n_iterations + 1, 1);

    time1(1) = 0;
    i1(1) = i1_initial;
    vc(1) = vc_initial;

    for n = 2:(n_iterations + 1)
        time1(n) = time1(n-1) + dt;
        l_dt = l / dt;
        c_dt = c * dt;
        i1(n) = ((i1(n-1) * (l_dt - r / 2 - dt / (2 * c))) + vb - vc(n-1)) / (l_dt + r / 2 + dt / (2 * c));
        vl(n) = ((i1(n) - i1(n-1)) / dt) * l;
        vc(n) = vc(n-1) + (((i1(n) + i1(n-1)) / 2) * dt) / c;
    end
end