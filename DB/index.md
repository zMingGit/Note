`sqlite3`:

```
CREATE INDEX IF NOT EXISTS FileOpsStat_timestamp ON FileOpsStat (timestamp)

```


`mysql`:

`
ALTER TABLE `FileOpsStat` ADD INDEX `fileopsstat_timestamp` (`timestamp`)
`