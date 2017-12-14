# Database code for the DB Forum, full solution!

import psycopg2

DBNAME = "news"
def get_query_results(query):
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(query)
  results = c.fetchall()
  db.close()
  return results

def get_popular_articles():
  """Return the most read articles from database"""
  return get_query_results("select title, count(*) from articles as t1 join log "
            "as t2 on t2.path = concat('/article/', t1.slug) group by title"
            " order by count(*) desc limit 3")

def get_popular_authors():
  """Return most popular authors from the 'database'"""
  return get_query_results("select name, sum(num_reads) from authors as a1 "
            "join (select title, t1.author, count(*) as num_reads "
            "from articles as t1 join log as t2 on t2.path = concat("
            "'/article/', t1.slug) group by title, t1.author) as a2 on a1.id"
            " = a2.author group by name order by sum(num_reads) desc")


def get_high_errors():
  """Return dates with high query failures from the 'database'"""
  return get_query_results("select date, not_found::numeric / (ok + not_found)"
            "::numeric as total_queries from status_table where not_found"
            "::numeric / (ok + not_found)::numeric > 0.01")

