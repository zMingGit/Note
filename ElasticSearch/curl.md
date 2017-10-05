## test custom analysis
```
curl -XPOST '172.16.3.178:9200/repofiles/_analyze?pretty' -H 'Content-Type: application/json' -d'
{
  "analyzer": "seafile_file_name_ngram_analyzer",
  "text": "123"
}
'
```

https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-custom-analyzer.html

----




## put custom analysis
curl -XPUT '172.16.3.176:9200/repo_files?pretty' -H 'Content-Type: application/json' -d'
{
  "settings": {                        
    "analysis": {                  
      "analyzer": {
        "cuu": {
          "type":      "custom",
          "tokenizer": "cu_t",
          "filter": [
            "lowercase"
          ]
        }
      },
      "tokenizer": {
          "cu_t": {
              "type": "nGram",
              "min_gram": "1",
              "max_gram": "4",
              "token_chars": ["letter", "digit"]
          }
      }
    }
  }
}
'




curl -XGET '192.168.1.116:9200/_search' -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
      "content": {
        "minimum_should_match": "80%",
        "query": "script"
      }
    }
  }
}'