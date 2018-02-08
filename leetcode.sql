# https://leetcode.com/problems/employees-earning-more-than-their-managers/description/

-- +----+-------+--------+-----------+
-- | Id | Name  | Salary | ManagerId |
-- +----+-------+--------+-----------+
-- | 1  | Joe   | 70000  | 3         |
-- | 2  | Henry | 80000  | 4         |
-- | 3  | Sam   | 60000  | NULL      |
-- | 4  | Max   | 90000  | NULL      |
-- +----+-------+--------+-----------+

-- +----------+
-- | Employee |
-- +----------+
-- | Joe      |
-- +----------+

# Write your MySQL query statement below
SELECT
    Name AS Employee
FROM (
    SELECT
        Employee.Id,
        Employee.Name,
        Employee.Salary AS ES,
        Manager.Salary AS MS,
        Manager.ManagerId
    FROM
        Employee AS Employee
    INNER JOIN
        Employee AS Manager
        ON Manager.Id = Employee.ManagerId
    WHERE
        Employee.Salary > Manager.Salary
) AS E