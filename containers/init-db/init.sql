USE alert_hub_zabbix;

CREATE TABLE IF NOT EXISTS zabbix_events (
                                      eventid INT PRIMARY KEY,
                                      source TINYINT,
                                      object TINYINT,
                                      objectid INT,
                                      clock BIGINT,
                                      value TINYINT,
                                      acknowledged TINYINT,
                                      ns BIGINT,
                                      name VARCHAR(255),
    severity TINYINT
    );