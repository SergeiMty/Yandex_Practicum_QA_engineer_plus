-- =========================================================
-- SQL PORTFOLIO (Practicum tasks) - Sergey Timofeev
-- DB dialect used in trainer: PostgreSQL-like
-- ToC:
--   [Q001] Count closed companies
--   [Q002] Funding totals for US news companies (sorted desc)
--   [Q003] People whose network_username starts with 'Silver'
--   [Q004] People with 'money' in username and last name starts with 'K'
--   [Q005] Sum of funding_total by country (desc)
--   [Q006] People and their education institution (LEFT JOIN)
--   [Q007] Sum of cash acquisitions 2011–2013
--   [Q008] Top-10 countries by avg invested companies (2010–2012), min>0
-- =========================================================


-- ========== [Q001] Count closed companies ==========
-- Goal: посчитать сколько компаний закрылось
-- Tables: company(status)
SELECT COUNT(*) AS closed_cnt
FROM company
WHERE status LIKE '%closed%';


-- ========== [Q002] Funding totals for US news companies (sorted desc) ==========
-- Goal: отобразить количество привлечённых средств для новостных компаний США
-- Tables: company(category_code, country_code, funding_total)
-- Note: в тренажёре поле funding_total текстовое; делаем CAST в int
SELECT CAST(funding_total AS INT) AS funding_total_int
FROM company
WHERE category_code = 'news' AND country_code = 'USA'
ORDER BY funding_total DESC;


-- ========== [Q003] Users with 'Silver*' in network_username ==========
-- Goal: имя, фамилия и username, начинающийся на 'Silver'
-- Tables: people(first_name, last_name, network_username)
SELECT
    first_name,
    last_name,
    network_username
FROM people
WHERE network_username LIKE 'Silver%';


-- ========== [Q004] Users whose username contains 'money' and last name starts with 'K' ==========
-- Goal: вывести всю информацию о таких людях
-- Tables: people(*, network_username, last_name)
SELECT *
FROM people
WHERE network_username LIKE '%money%'
  AND  last_name       LIKE 'K%';


-- ========== [Q005] Sum of funding_total by country (desc) ==========
-- Goal: для каждой страны показать общую сумму инвестиций компаний; отсортировать по сумме (убыв.)
-- Tables: company(country_code, funding_total)
SELECT
    country_code,
    SUM(funding_total) AS total_funding
FROM company
GROUP BY country_code
ORDER BY SUM(funding_total) DESC;


-- ========== [Q006] People with education institution (LEFT JOIN) ==========
-- Goal: вывести имя, фамилию сотрудника стартапа и учебное заведение (если есть)
-- Tables: people p(id, first_name, last_name), education e(person_id, institution)
SELECT
    p.first_name,
    p.last_name,
    e.institution
FROM people AS p
LEFT JOIN education AS e
  ON p.id = e.person_id;


-- ========== [Q007] Sum of cash acquisitions 2011–2013 ==========
-- Goal: найти общую сумму сделки по покупке, только наличные, 2011..2013 включительно
-- Tables: acquisition(price_amount, term_code, acquired_at)
SELECT SUM(price_amount) AS total_cash_amount
FROM acquisition
WHERE term_code = 'cash'
  AND acquired_at BETWEEN '2011-01-01' AND '2013-12-31';


-- ========== [Q008] Top-10 countries by avg invested companies (2010–2012), min>0 ==========
-- Goal: страны, в которых фонды чаще инвестировали в стартапы; 2010..2012; исключить min=0; top-10 по AVG
-- Tables: fund(country_code, invested_companies, founded_at)
SELECT
    country_code,
    MIN(invested_companies) AS min_invested_companies,
    MAX(invested_companies) AS max_invested_companies,
    AVG(invested_companies) AS avg_invested_companies
FROM fund
WHERE EXTRACT(YEAR FROM founded_at) BETWEEN 2010 AND 2012
GROUP BY country_code
HAVING MIN(invested_companies) > 0
ORDER BY AVG(invested_companies) DESC,
         country_code
LIMIT 10;
