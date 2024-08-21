# BOT de monitoramento e repasse de mensagens v1.0

from telethon import TelegramClient, events
from time import sleep
import requests
from senhas import api_hash, api_id

sessao = 'Repassar Mensagem'

async def main(): # Repasse das mensagens
    print('Monitoramento iniciado....')
    async with TelegramClient(sessao, api_id, api_hash) as client:
        @client.on(events.NewMessage(chats=[1002196768298]))   # Espera chegar novas mensagens e quando chega ele chama alguma função
        async def enviar_mensagem(event):
            if event.media:
                await client.send_file(-1002177665054, file=event.media,caption=event.raw_text) # Envia midia
            else:
                await client.send_message(-1002177665054, event.raw_text) # ID de onde deve ir a mensagem enviada e a mensagem a ser enviada
        await client.run_until_disconnected()

# Para rodar a função principal
import asyncio
asyncio.run(main())