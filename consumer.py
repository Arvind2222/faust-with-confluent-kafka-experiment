#!/usr/bin/env python
import faust

app = faust.App(
    'hello-world',
    broker='kafka://localhost:9092',
)

greetings_topic = app.topic('greetings', value_type=str)


@app.agent(greetings_topic)
async def print_greetings(greetings):
    async for greeting in greetings:
        print('hi {}'.format(greeting))

if __name__ == '__main__':
    app.main()
