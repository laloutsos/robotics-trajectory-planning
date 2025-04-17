tf = 50;
t1 = 0:0.01:5;
t2 = 5.01:0.01:tf+5;
t3 = tf+5:0.01:55.185;



position1 = zeros(size(t1));
velocity1 = zeros(size(t1));
acceleration1 = zeros(size(t1));

position2 = ((3*6)/tf^2)*((t2-5).^2) - (12/tf^3)*((t2-5).^3);
velocity2 = (36*(t2-5).*(tf-t2+5))/tf^3;
acceleration2 = (36*(tf-2*(t2-5)))/tf^3;


position3 = ones(size(t3)).*6;
velocity3 = zeros(size(t3));
acceleration3 = zeros(size(t3));


position = [position1, position2, position3];
velocity = [velocity1, velocity2, velocity3];
acceleration = [acceleration1, acceleration2, acceleration3];


t = [t1, t2, t3];


subplot(3, 1, 1);
plot(t, position);
xlabel('Time (s)');
ylabel('Position');
title('Position vs Time');


subplot(3, 1, 2);
plot(t, velocity);
xlabel('Time (s)');
ylabel('Velocity (m/s)');
title('Velocity vs Time');


subplot(3, 1, 3);
plot(t, acceleration);
xlabel('Time (s)');
ylabel('Acceleration (m/s^2)');
title('Acceleration vs Time');
