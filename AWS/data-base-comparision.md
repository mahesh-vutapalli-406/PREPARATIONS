**AWS Database Services Comparison Table**
------------------------------------------

| **Database** | **Type** | **Use Case** | **Server/Serverless** | **Pricing Model** | **Cross-Region Replication** | **Best For** |
| --- | --- | --- | --- | --- | --- | --- |
| **RDS (Relational Database Service)** | SQL (Relational) | General-purpose relational DBs | **Server-based** | **On-Demand & Provisioned** | ✅ Yes (Multi-AZ & Read Replicas) | Traditional applications requiring SQL databases |
| **Aurora** | SQL (MySQL/PostgreSQL) | High-performance, scalable relational DB | **Both (Aurora Serverless v2 available)** | **On-Demand & Provisioned** | ✅ Yes (Global Database feature) | Enterprise-grade MySQL/PostgreSQL workloads |
| **DynamoDB** | NoSQL (Key-Value) | Serverless, ultra-low-latency NoSQL DB | **Serverless** | **On-Demand & Provisioned (Read/Write Capacity)** | ✅ Yes (Global Tables) | High-speed NoSQL workloads, IoT, gaming |
| **Redshift** | Data Warehouse | Analytics & Business Intelligence (BI) | **Server-based** | **On-Demand & Reserved Instances** | ✅ Yes (Cross-region snapshot copy) | Large-scale data analytics and OLAP workloads |
| **ElastiCache (Redis, Memcached)** | In-Memory NoSQL | Caching for high-speed applications | **Server-based** | **On-Demand** | ❌ No (Only manual backups across regions) | Speeding up database queries, session management |
| **Neptune** | Graph Database | Social networks, fraud detection | **Server-based** | **On-Demand & Provisioned** | ✅ Yes (Read Replicas) | Highly connected data like knowledge graphs |
| **DocumentDB** | NoSQL (Document) | MongoDB-compatible document storage | **Server-based** | **On-Demand & Provisioned** | ✅ Yes (Global Clusters) | Semi-structured JSON-like document storage |
| **Timestream** | Time-Series NoSQL | IoT, logs, real-time data processing | **Serverless** | **Pay-per-use (Inserts & Queries)** | ✅ Yes (Cross-region replication supported) | Sensor data, IoT, financial data |
| **Keyspaces (Managed Cassandra)** | NoSQL (Columnar) | Cassandra-compatible scalable DB | **Serverless** | **Pay-per-use** | ✅ Yes (Multi-Region replication) | Large-scale column-based NoSQL workloads |

* * * * *

**Pricing Comparison by Database Type**
---------------------------------------

| **Database** | **Pricing Model** | **Estimated Cost** |
| --- | --- | --- |
| **RDS (MySQL/PostgreSQL/SQL Server)** | **On-Demand**: Pay for instance & storage **Provisioned**: Reserved instance for savings | **$0.017/hour - $10/hour** (varies by instance) |
| **Aurora** | **On-Demand**: Per second **Serverless**: Pay per capacity unit | **$0.10 - $1.50/hour** (varies by usage) |
| **DynamoDB** | **On-Demand**: Pay per request **Provisioned**: Fixed read/write capacity | **$1.25/million writes, $0.25/million reads** |
| **Redshift** | **On-Demand**: Per compute node **Reserved**: 1-3 year commitment | **$0.25 - $13/hour per node** |
| **ElastiCache (Redis/Memcached)** | **On-Demand**: Per node | **$0.02 - $1.50/hour per node** |
| **Neptune** | **On-Demand**: Per instance **Provisioned**: Reserved instance | **$0.10 - $2/hour** |
| **DocumentDB** | **On-Demand**: Per instance & I/O **Provisioned**: Reserved | **$0.10 - $2/hour per instance** |
| **Timestream** | **Pay-per-use**: Inserts & queries **Storage**: Pay per GB | **$0.50/GB-month + queries cost** |
| **Keyspaces (Cassandra)** | **Pay-per-use**: Read/write requests | **$1.45/million writes, $0.29/million reads** |

* * * * *

**Key Takeaways: When to Use Which AWS Database Service?**
----------------------------------------------------------

✅ **Use RDS** → When you need a traditional relational database (MySQL, PostgreSQL, SQL Server, etc.).\
✅ **Use Aurora** → When you need **high-performance relational databases** with **auto-scaling & high availability**.\
✅ **Use DynamoDB** → When you need **serverless NoSQL**, fast lookups, and **high scalability**.\
✅ **Use Redshift** → When you need **big data analytics** and **data warehousing**.\
✅ **Use ElastiCache** → When you need **low-latency caching** for frequently accessed data.\
✅ **Use Neptune** → When you need **graph-based relationships** for social networks, fraud detection, or knowledge graphs.\
✅ **Use DocumentDB** → When you need a **MongoDB-compatible document store** for JSON-based data.\
✅ **Use Timestream** → When you need a **time-series database** for IoT and real-time analytics.\
✅ **Use Keyspaces** → When you need **Cassandra-compatible NoSQL** at scale.