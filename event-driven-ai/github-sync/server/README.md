## What is Kafka

Apache Kafka is a distributed event store and stream-processing platform.

### ZooKeeper Basics

* Open Source Apache Project
* Distributed Key Value Store
* Maintains configuration information
* Stores ACLs and Secrets
* Enables highly reliable distributed coordination
* Provides distributed synchronization

## Topics

* Developers define Topics
* Producer <-> Topic: N to N Relation
* Unlimited Number of Topics
* Topics: Streams of "related" Messages in Kafka
  * Is a Logical Representation
  * Categorizes Messages into Groups

## Broker Basics

* Producer sends Messages to Brokers
* Brokers recieve and store Messages
* A Kafka cluster can have many Brokers
* Each Broker manages multiple Partitions

## Producer Basics

* Producers write data as messages
* Can be written in any language
* Command Line Producer Tool

## Consumer Basics

* Consumers pull messages from. 1....n topcis
* New inflowing messages are automatically retrieved
* Consumer offset
  * Keeps track of the last messages read
  * Is stored in special topic
* CLI tools exist to read from cluster

# Lesson Glossary

* Stream - An unboundecd sequence of ordered, immutable datra
* Stream Processing - Continual calculations performed on one or more streams
* Immutable Data - Data that cannot be change once it has been created
* Event - An immutable fact regarding something that has occurred in our system.
* Broker (Kakfa) - A single member server of the Kafka cluster
* Cluster (Kafka) - A group of one or more Kafka Brokers working together to satisfy Kafka production and consumption.
* Node - A single computing instance. May be physical, as in a server in a datacenter, or virtual, as an instance might be in AWS, GCP, or Azure.
* Zookeeper - Used by Kafka Brokers to determine which broker is the leader of a given partition and topc, as well as track cluster membership and configuration for kafka.
* Data Partition (Kakfka) - Kafka topics consist of one or more partitions. A partition is a log which provides ordering gurantees for all of the data contained withing it. Partitions are chosen by hashing key values.
