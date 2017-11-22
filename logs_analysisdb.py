# Database code for the DB Forum, full solution!

import psycopg2, bleach

DBNAME = "news"

def get_popular_articles():
  """Return the most read articles from database"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select title, count(*) from articles as t1 join log "
            "as t2 on position (t1.slug in t2.path)<>0 group by title"
            " order by count(*) desc limit 3")
  articles = c.fetchall()
  db.close()
  return articles

def get_popular_authors():
  """Return most popular authors from the 'database'"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select name, sum(num_reads) from authors as a1 "
            "join (select title, t1.author, count(*) as num_reads "
            "from articles as t1 join log as t2 on position (t1.slug "
            "in t2.path)<>0 group by title, t1.author) as a2 on a1.id"
            " = a2.author group by name order by sum(num_reads) desc")
  authors = c.fetchall()
  db.close()
  return authors

def get_high_errors():
  """Return dates with high query failures from the 'database'"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select * from (select date, not_found/total_queries "
            "as percentage from (select date, not_found, sum(ok + not_found)"
            " as total_queries from status_table group by date, not_found)"
            " as t1) as t2 where percentage > 0.01;")
  dates = c.fetchall()
  db.close()
  return dates
