tf = 5;
t1 = 0:0.01:tf;
t2 = tf + 0.01:0.01:tf + 45;
t3 = tf + 45.01:0.01:tf + 45 + tf;


angular_velocity_1 = (2.76 * (tf - t1) .* t1) ./ tf.^3;
angular_velocity_2 = zeros(size(t2));
angular_velocity_3 = (6 * 1.08 .* (t3-tf-45) .* (tf - t3+tf+45)) ./ tf.^3;


t = [t1, t2, t3];
angular_velocity = [angular_velocity_1, angular_velocity_2, angular_velocity_3];


theta_1 = (0.46 * (3 * tf - 2 * t1) .* t1.^2) ./ tf^3;
theta_2 = ones(size(t2)) * theta_1(end);
theta_3 = 0.46 + ((3 * 1.08 .* (t3-tf-45).^2) ./ tf^2) - (2 * 1.08 .* (t3-tf-45).^3) ./ tf^3;

theta = [theta_1, theta_2, theta_3];
accel1 = (2.76 * (tf - 2 * t1)) ./ tf^3;
accel2 = zeros(size(t2));
accel3 = (6 * 1.08 * (tf - 2 * (t3-tf-45))) ./ tf^3;
acceleration = [accel1, accel2, accel3];


subplot(3, 1, 1);
plot(t, angular_velocity);
xlabel('Time (s)');
ylabel('Angular Velocity (rad/s)');
title('Angular Velocity vs. Time');
grid on;


subplot(3, 1, 2);
plot(t, theta);
xlabel('Time (s)');
ylabel('Orientation (rad)');
title('Orientation vs. Time');
grid on;

subplot(3, 1, 3);
plot(t, acceleration);
xlabel('Time (s)');
ylabel('Angular Acceleration (rad/s^2)');
title('Angular Acceleration vs. Time');
grid on;
