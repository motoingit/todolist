-- Drop the table if it already exists to start fresh
DROP TABLE IF EXISTS todo;

-- Create the table structure based on your original db file
CREATE TABLE todo (
	sno INTEGER NOT NULL, 
	title VARCHAR(200) NOT NULL, 
	"desc" VARCHAR(500) NOT NULL, 
	date_created DATETIME, 
	PRIMARY KEY (sno)
);

-- Insert some sample data into the table
INSERT INTO todo (sno, title, "desc", date_created) VALUES
(1, 'Buy Groceries', 'Need to buy milk, bread, eggs, and fruits for the week.', '2025-09-28 10:00:00'),
(2, 'Finish Project Report', 'Complete the final draft of the Q3 sales report and send it for review.', '2025-09-28 11:30:00'),
(3, 'Schedule Dentist Appointment', 'Call the clinic to book a routine check-up for next week.', '2025-09-28 14:00:00'),
(4, 'Go for a Run', '30-minute jog around the park in the evening.', '2025-09-28 17:45:00'),
(5, 'Pay Electricity Bill', 'The bill is due tomorrow. Pay online via the portal.', '2025-09-28 20:15:00');