from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.sql_database import SQLDatabase

import sqlite3
import getpass
import os
from dotenv import load_dotenv
load_dotenv()

#環境変数を取得
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_api_model = os.getenv("OPENAI_API_MODEL")

# ChatGPT-3.5のモデルのインスタンスの作成
llm = ChatOpenAI(model_name=openai_api_model)

# db = sqlite3.connect('Chinook.db')
db = SQLDatabase.from_uri("sqlite:///Chinook.db")

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# SQLデータベースと対話するエージェントを作成
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)

agent_executor.run("質問内容")



