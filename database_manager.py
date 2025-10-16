import os
from dotenv import load_dotenv
import psycopg2
from typing import Dict

load_dotenv()

class DatabaseManager:
    def __init__(self):
        pass
    
    def get_db_connection(self):
        try:
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                database=os.getenv('DB_NAME', 'postgres'),
                user=os.getenv('DB_USER', 'postgres'),
                password=os.getenv('DB_PASSWORD', 'password'),
                port=os.getenv('DB_PORT', '5432')
            )
            return conn
        except Exception as e:
            print(f"Database connection error: {e}")
            return None
    
    def save_color_frequencies(self, color_frequencies: Dict[str, int]):
        conn = self.get_db_connection()
        if conn is None:
            print("Failed to connect to database.")
            return
        
        try:
            cursor = conn.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS color_frequencies (
                    id SERIAL PRIMARY KEY,
                    color VARCHAR(50) UNIQUE NOT NULL,
                    frequency INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            cursor.execute("DELETE FROM color_frequencies")
            
            for color, freq in color_frequencies.items():
                cursor.execute("""
                    INSERT INTO color_frequencies (color, frequency) 
                    VALUES (%s, %s)
                """, (color, freq))
            
            conn.commit()
            print(f"SUCCESS: Saved {len(color_frequencies)} colors to database")
            
            cursor.execute("SELECT color, frequency FROM color_frequencies ORDER BY frequency DESC")
            records = cursor.fetchall()
            print("SAVED DATA:")
            print("------------------------------")
            for color, freq in records:
                print(f"  {color}: {freq}")
            print("------------------------------")
                
        except Exception as e:
            print(f"ERROR: {e}")
            conn.rollback()
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def test_connection(self):
        conn = self.get_db_connection()
        if conn:
            print("SUCCESS: Database connection successful!")
            conn.close()
            return True
        else:
            print("ERROR: Database connection failed!")
            return False