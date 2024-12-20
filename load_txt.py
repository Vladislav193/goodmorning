from database import AsyncSessionLocal


async def load_texts(filename, model):
    with open(filename, 'r', encoding="utf-8") as file:
        texts = file.readlines()
    async with AsyncSessionLocal() as session:
        try:
            for text in texts:
                text = text.strip()
                if text:
                    db_text = model(text=text)
                    session.add(db_text)
            await session.commit()
        except Exception as e:
            await session.rollback()
            print(f"Ошибка при загрузке данных: {e}")
        finally:
            await session.close()