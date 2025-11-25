INSERT INTO Users (username, password_hash)
VALUES
('alice_chen', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
('bob_wong', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
('cindy_liu', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
('david_zhang', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
('ella_sun', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
('frank_guo', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
('grace_hu', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
('henry_li', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
('ivy_feng', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
('jack_ma', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92');

INSERT INTO Visitor_Info (user_id, name, phone, affiliation)
VALUES
(1, 'Alice Chen', '13812340001', 'Tencent'),
(2, 'Bob Wong', '13812340002', 'Huawei'),
(3, 'Cindy Liu', '13812340003', 'CUHK Alumni'),
(4, 'David Zhang', '13812340004', 'Bytedance'),
(5, 'Ella Sun', '13812340005', 'Shenzhen University'),
(6, 'Frank Guo', '13812340006', 'Lenovo'),
(7, 'Grace Hu', '13812340007', 'Alibaba'),
(8, 'Henry Li', '13812340008', 'SF Express'),
(9, 'Ivy Feng', '13812340009', 'Tencent'),
(10, 'Jack Ma', '13812340010', 'ZJU');

INSERT INTO Admins (username, password_hash, phone)
VALUES
('admin_1', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', '15000000001'),
('admin_2', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c922', '15000000002'),
('admin_3', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', '15000000003');

INSERT INTO Reservations 
(user_id, visit_date, visit_time, location, purpose, status)
VALUES
(1, '2025-11-23', '10:00', 'Academic Building A', 'Campus Tour', 'pending'),
(2, '2025-11-23', '14:00', 'Library', 'Research Meeting', 'pending'),
(3, '2025-11-23', '09:30', 'Administration Building', 'Document Submission', 'pending'),
(4, '2025-11-23', '15:00', 'Academic Building B', 'Professor Meeting', 'pending'),
(5, '2025-11-23', '11:00', 'Library', 'Project Discussion', 'pending'),
(6, '2025-11-23', '13:30', 'Startup Center', 'Innovation Visit', 'pending'),
(7, '2025-11-23', '10:30', 'Faculty Block E', 'Guest Lecture', 'pending'),
(8, '2025-11-23', '16:00', 'Library', 'Book Donation', 'pending'),
(9, '2025-11-23', '10:00', 'Academic Building C', 'Student Event', 'pending'),
(10,'2025-11-23', '14:00', 'Gymnasium', 'Sports Facility Tour', 'pending');

INSERT INTO Reservations
(user_id, visit_date, visit_time, location, purpose, status, admin_id, review_comment)
VALUES
(1, '2025-02-20', '09:00', 'Academic Building A', 'Project Meeting', 'approved', 1, 'Approved'),
(2, '2025-02-21', '10:30', 'Library', 'Academic Research', 'approved', 1, 'Approved'),
(3, '2025-02-22', '14:00', 'Gymnasium', 'Sports Event', 'approved', 2, 'Welcome'),
(4, '2025-02-23', '15:30', 'Academic Building B', 'Lab Visit', 'approved', 2, 'Approved'),
(5, '2025-02-24', '11:00', 'Faculty Block E', 'Interview', 'approved', 1, 'Approved'),
(6, '2025-02-25', '09:30', 'Library', 'Study Collaboration', 'approved', 1, 'Approved'),
(7, '2025-02-26', '13:00', 'Startup Center', 'Tech Exchange', 'approved', 2, 'Approved'),
(8, '2025-02-27', '14:30', 'Academic Building C', 'Event Preparation', 'approved', 2, 'Approved'),
(9, '2025-02-28', '16:00', 'Administration Building', 'Business Visit', 'approved', 1, 'Approved'),
(10,'2025-03-01', '09:00', 'Gymnasium', 'Sports Tour', 'approved', 1, 'Enjoy your visit');

INSERT INTO Reservations
(user_id, visit_date, visit_time, location, purpose, status, admin_id, review_comment)
VALUES
(1, '2025-02-15', '10:00', 'Academic Building A', 'Unauthorized Access', 'denied', 3, 'Not eligible'),
(2, '2025-02-16', '11:00', 'Library', 'Incomplete Info', 'denied', 3, 'Need more details'),
(3, '2025-02-17', '13:00', 'Faculty Block E', 'Late Request', 'denied', 3, 'Too late'),
(4, '2025-02-18', '15:00', 'Startup Center', 'Invalid Reason', 'denied', 1, 'Purpose unclear'),
(5, '2025-02-19', '09:30', 'Academic Building C', 'Conflict', 'denied', 2, 'Schedule conflict'),
(6, '2025-02-20', '10:00', 'Library', 'Double Booking', 'denied', 3, 'Already booked'),
(7, '2025-02-21', '16:00', 'Gymnasium', 'Capacity Full', 'denied', 1, 'No availability'),
(8, '2025-02-22', '14:30', 'Faculty Block E', 'Security Issue', 'denied', 2, 'Not allowed'),
(9, '2025-02-23', '11:00', 'Administration Building', 'Policy Restriction', 'denied', 2, 'Restricted area'),
(10,'2025-02-24', '15:00', 'Academic Building B', 'Insufficient Info', 'denied', 1, 'More details needed');

