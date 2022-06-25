<?php
class History
{

    // database connection and table name
    private $conn;
    private $table_name = "history";

    // constructor with $db as database connection
    public function __construct($db)
    {
        $this->conn = $db;
    }
    // list history
    function list()
    {
        // select all query
        $query = "SELECT
                    *
                FROM
                    " . $this->table_name . " ";
        // prepare query statement
        $stmt = $this->conn->prepare($query);
        // execute query
        $stmt->execute();
        return $stmt;
    }
}
