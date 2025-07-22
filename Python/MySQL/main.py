from create_table import create_table
from insert_data import insert_data
from view_data import view_data
from drop_table import drop_table
from update_data import update_data



def main():
    drop_table()
    create_table()
    insert_data()
    view_data()
    update_data()

if __name__ == "__main__":
    main()