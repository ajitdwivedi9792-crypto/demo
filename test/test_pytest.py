df=spark.table("source_order")
def test_source_order_table_exists():
    assert spark.catalog.tableExists("source_order"), "source_order table does not exist"

def test_verify_row_count():
    
   
    assert df.count() == 3, f"Expected 3 rows but found ({df.count()})"

def test_verify_schema():
    expected_column = ["order_id","customer","amount"]
    assert spark.catalog.tableExists("source_order"), "source_order table does not exist"

def test_verfiy_null():
    null_count=df.filter("order_id is null").count()
    assert null_count == 0, f"Expected no null values in order_id column but found {null_count} null values"

def test_verify_specific_record():
    record_count = df.filter("order_id == 1 and customer = 'john wick' and amount = 500").count()

    assert record_count == 1, f"Expected order_id value to be 1 but found {order_id}"


    #       environment_key: default
          
    #   environments:
    #     - environment_key: default
    #       spec:
    #         client: "1"