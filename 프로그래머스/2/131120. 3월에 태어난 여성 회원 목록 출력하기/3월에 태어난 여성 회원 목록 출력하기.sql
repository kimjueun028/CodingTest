SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE (GENDER='W') and (month(DATE_OF_BIRTH)=3) and (TLNO IS NOT NULL)