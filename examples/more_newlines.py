# A more complex query with multipe joins
import sqlparse

if __name__ == '__main__':

    sql = """
        select tab1.class,tab2.class2,count(*) as cnt, coalese(t.a,    b)*sqrt(365/ 7)* 10000 as c
        from TAB1 inner join tab2 t on tab2.id = TAB1.id and tab2.date = '2020-02-20'
        left join tab3 s on tab3.myid = tab1.myid and tab3.region = 'US'
        where tab1.sales > 2000 group by tab1.class,tab2.class2
        """

    print(sqlparse.format(sql,
        reindent=True,
        # strip_whitespace=True,
        keyword_case='lower',
        identifier_case='lower',
        comma_first=True,
        use_space_around_operators=True,
        more_newlines=True,
        # indent_width=4,
        ))
