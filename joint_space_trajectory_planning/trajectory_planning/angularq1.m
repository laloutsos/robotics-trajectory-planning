
theta_0 = 0;
theta_f = 67.5;



tb = 2;
tf =20;


a = 15/8


t1 = linspace(0, tb, 100);
t2 = linspace(tb, tf-tb, 100);
t3 = linspace(tf-tb, tf, 100);


theta1 = theta_0 + (1/2)* a * t1.^2;
theta2 = theta_0 + (1/2)* a * tb^2 + a * tb* (t2 - tb);
theta3 = theta_f - (1/2) * a * (tf - t3).^2;

theta1_dot =  a .* t1;
theta2_dot = a * tb * ones(size(t2));
theta3_dot = a * tb - a * (t3 - (tf - tb));

theta_double_dot1 =  a*ones(size(t1));
theta_double_dot2 = zeros(size(t2));
theta_double_dot3 = - a*ones(size(t3)) ;



t = [t1, t2, t3];
theta = [theta1, theta2, theta3];
theta_dot= [theta1_dot,theta2_dot,theta3_dot];
theta_double_dot=[theta_double_dot1,theta_double_dot2,theta_double_dot3];

subplot(3,1,1);
plot(t, theta, 'b', 'LineWidth', 2);
xlabel('Χρόνος (s)');
ylabel('Γωνία (deg)');
title('Τροχιά Άρθρωσης q1 από 0° έως 67°');

subplot(3,1,2)
plot(t, theta_dot, 'b', 'LineWidth', 2);
xlabel('Χρόνος (s)');
ylabel('Γωνιακή Ταχύτητα (deg/s)');
title('Γωνιακή ταχύτητα q1 από 0° έως 67°');
grid on;


subplot(3,1,3)
plot(t, theta_double_dot, 'b', 'LineWidth', 2);
xlabel('Χρόνος (s)');
ylabel('Γωνιακή επιτάχυνση (deg/s^2)');
title('Γωνιακή Επιταχυνση q1 από 0° έως 67°');
grid on;
