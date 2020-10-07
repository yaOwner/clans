class Clans(commands.Cog):
	def __init__(self, Bot):
		self.Bot = Bot


	@commands.group()
	async def clan(self, ctx):
		pass

	@clan.command()
	async def buy(self, ctx, *, name = None):
		if ctx.channel.id == 668447958303506432 or ctx.channel.id == 730332130575384596:

			if name is None:
				emb = discord.Embed(description = 'Введите название клана!', timestamp = datetime.datetime.utcnow())
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

				await ctx.message.delete()

			elif len(name) > 25:
				emb = discord.Embed(description = 'Имя клана слишком длиное!', timestamp = datetime.datetime.utcnow())
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

				await ctx.message.delete()

			else:
				balance = db['test']
				if balance.find_one({"_id": ctx.author.id})['cash'] < 30000:
					emb = discord.Embed(description = 'Недостаточно денег!', timestamp = datetime.datetime.utcnow())
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

					await ctx.message.delete()

				else:
					
					if clan.count_documents({"name": name}):
						emb = discord.Embed(description = 'Такой клан уже существует!', timestamp = datetime.datetime.utcnow())
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)

						await ctx.message.delete()

					else:
						if clan2.count_documents({"_id": ctx.author.id}):
							emb = discord.Embed(description = f'Вы уже в клане ', timestamp = datetime.datetime.utcnow())
							emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
							await ctx.send(embed = emb)

							await ctx.message.delete()

						else:
							emb = discord.Embed(description = 'Вы успешно создали клан!', timestamp = datetime.datetime.utcnow())
							emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
							await ctx.send(embed = emb)

							balance = db['test']

							clan.insert_one({"owner": ctx.author.id, "name": name, "bio": 'Пусто', "flag": None, "cash": 0, "data": datetime.datetime.today(), "members": 1})
							clan2.insert_one({"_id": ctx.author.id, "name": name, "clanid": ctx.author.id})

							newcash2 = balance.find_one({"_id": ctx.author.id})['cash'] - 30000
							balance.update_one({"_id": ctx.author.id}, {"$set": {"cash": newcash2}}) 


		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()


	@clan.command()
	async def info(self, ctx, *, name = None):
		if ctx.channel.id == 668447958303506432:

			if name is None:
				emb = discord.Embed(description = 'Введите название клана!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:

				try:
					if clan.count_documents({"name": name}):
						for x in clan.find({"name": name}):

							emb = discord.Embed(timestamp = datetime.datetime.utcnow())

							emb.add_field(name = '`Описание:⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`', value = f'```fix\n{x["bio"]}```', inline = False)

							emb.add_field(name = '`Казна клана:⠀⠀⠀⠀`', value = f'```fix\n{x["cash"]}```')

							emb.add_field(name = '`Владелец:⠀⠀⠀⠀⠀⠀⠀⠀`', value = f'```yaml\n{self.Bot.get_user(x["owner"])}```')
							emb.add_field(name = '`Участников:⠀⠀⠀⠀⠀⠀`', value = f'```yaml\n{x["members"]}```')

							emb.add_field(name = '`Дата создания:⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`', value = f'```md\n#{x["data"]}```', inline = False)


							emb.set_thumbnail(url = x["flag"])
							emb.set_author(icon_url = '{}'.format(x["flag"]), name = f'Clan profile | {name}')

							await ctx.send(embed = emb)
					else:
						emb = discord.Embed(description = 'Такого клана не существует!', timestamp = datetime.datetime.utcnow())
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)

				except:
					if clan.count_documents({"name": name}):
						
						for x in clan.find({"name": name}):

							emb = discord.Embed(timestamp = datetime.datetime.utcnow())

							emb.add_field(name = '`Описание:⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`', value = f'```fix\n{x["bio"]}```', inline = False)

							emb.add_field(name = '`Казна клана:⠀⠀⠀⠀`', value = f'```fix\n{x["cash"]}```')

							emb.add_field(name = '`Владелец:⠀⠀⠀⠀⠀⠀⠀⠀`', value = f'```yaml\n{self.Bot.get_user(x["owner"])}```')
							emb.add_field(name = '`⠀⠀⠀Участников:⠀⠀⠀`', value = f'```yaml\n{x["members"]}```')

							emb.add_field(name = '`Дата создания:⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`', value = f'```md\n#{x["data"]}```', inline = False)

							emb.set_thumbnail(url = self.Bot.get_user(x["owner"]).avatar_url)
							emb.set_author(icon_url = '{}'.format(self.Bot.get_user(x["owner"]).avatar_url), name = f'Clan profile | {name}')

							await ctx.send(embed = emb)

					else:
						emb = discord.Embed(description = 'Такого клана не существует!', timestamp = datetime.datetime.utcnow())
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def banner(self, ctx, link = None):
		if ctx.channel.id == 668447958303506432:

			if link is None:
				emb = discord.Embed(description = 'Укажите ссылку на баннер для клана!', timestamp = datetime.datetime.utcnow())
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:				
				try:
					if clan.count_documents({"owner": ctx.author.id}):
						balance = db['test']

						if balance.find_one({"_id": ctx.author.id})['cash'] > 5000:
								
							emb = discord.Embed(description = 'Вы поменяли баннер клана!', timestamp = datetime.datetime.utcnow())
							emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))

							emb.set_image(url = link)

							await ctx.send(embed = emb)
							await ctx.message.delete()

							name = clan.find_one({"owner": ctx.author.id})['name']
								
							clan.update_one({"name": name}, {"$set": {"flag": link}}) 

							newcash = balance.find_one({"_id": ctx.author.id})['cash'] - 5000
							balance.update_one({"_id": ctx.author.id}, {"$set": {"cash": newcash}}) 
							
						else:
								
							emb = discord.Embed(description = 'Недостаточно денег!', timestamp = datetime.datetime.utcnow())
							emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
							await ctx.send(embed = emb)
					else:
						emb = discord.Embed(description = 'Только глава может поменять баннер клана!', timestamp = datetime.datetime.utcnow())
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)

						await ctx.message.delete()		
				except:
					emb = discord.Embed(description = 'Уажите ссылку на картинку!', timestamp = datetime.datetime.utcnow())
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

					await ctx.message.delete()	
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def bio(self, ctx, *, bio = None):
		if ctx.channel.id == 668447958303506432:	
			if clan.count_documents({"owner": ctx.author.id}):

				if bio is None:
					emb = discord.Embed(description = 'Укажите описание!', timestamp = datetime.datetime.utcnow())
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

				elif len(bio) > 120:
					emb = discord.Embed(description = 'Слишком много символов(макс: 120)', timestamp = datetime.datetime.utcnow())
					emb.set_author(icon_url = '{}'.format(ctx.author.avatar_url), name = '{}'.format(ctx.author))

					await ctx.send(embed = emb)

				else:

					emb = discord.Embed(description = f'Вы поменяли описание вашего клана на:\n```fix\n{bio}```', timestamp = datetime.datetime.utcnow())
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

					name = clan.find_one({"owner": ctx.author.id})['name']

					clan.update_one({"name": name}, {"$set": {"bio": bio}}) 
			
			else:
				emb = discord.Embed(description = 'Только глава может поменять описание клана!', timestamp = datetime.datetime.utcnow())
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def invite(self, ctx, member: discord.Member = None):
		if ctx.channel.id == 668447958303506432:

			if member is None:
				emb = discord.Embed(description = 'Укажите пользователя!', timestamp = datetime.datetime.utcnow())
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:
				if clan.count_documents({"owner": ctx.author.id}):
					name = clan.find_one({"owner": ctx.author.id})['name']

					if not clan2.count_documents({"_id": member.id}):
							
						solutions = ['✅', '❌']
						emb = discord.Embed(title = f'Кланы {ctx.guild.name}', description = f'**{member}** хотите ли вы вступить в клан **{name}?**', timestamp = datetime.datetime.utcnow())
							
						message = await ctx.send(embed = emb)
							
						for x in solutions:
							await message.add_reaction(x)

						try:
							react, user = await self.Bot.wait_for('reaction_add', timeout= 30.0, check= lambda react, user: user == member and react.message.channel == ctx.channel and react.emoji in solutions)
						except asyncio.TimeoutError:
							emb = discord.Embed(description = 'Время на ответ вышло', timestamp = datetime.datetime.utcnow())
							emb.set_author(icon_url = '{}'.format(ctx.author.avatar_url), name = '{}'.format(ctx.author))

							await message.edit(embed = emb)
							await message.clear_reactions()
						else:
							if str(react.emoji) == '✅':
								await message.clear_reactions()

								emb = discord.Embed(title = f'Кланы {ctx.guild.name}', description = f'**{member}** вступил в клан **{name}!**', timestamp = datetime.datetime.utcnow())
								await message.edit(embed = emb)
								
								clan2.insert_one({"_id": member.id, "name": name, "clanid": ctx.author.id})

								for x in clan.find({"name": name}):
									members = x['members'] + 1
									
									clan.update_one({"name": name}, {"$set": {"members": members}}) 
									
							elif str(react.emoji) == '❌':
								await message.clear_reactions()

								emb = discord.Embed(title = f'Кланы {ctx.guild.name}', description = f'**{member}** отказался от приглашения!', timestamp = datetime.datetime.utcnow())

								await message.edit(embed = emb)

					else:

						emb = discord.Embed(description = 'Пользователь уже в клане!', timestamp = datetime.datetime.utcnow())
						emb.set_author(icon_url = '{}'.format(ctx.author.avatar_url), name = '{}'.format(ctx.author))
						await ctx.send(embed = emb)
				else:

					emb = discord.Embed(description = 'Только глава может приглашать людей!', timestamp = datetime.datetime.utcnow())
					emb.set_author(icon_url = '{}'.format(ctx.author.avatar_url), name = '{}'.format(ctx.author))
					await ctx.send(embed = emb)
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def owner(self, ctx, member: discord.Member = None):
		if ctx.channel.id == 668447958303506432:

			if member is None:
				emb = discord.Embed(description = 'Укажите пользователя!', timestamp = datetime.datetime.utcnow())
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:

				if not clan2.count_documents({"_id": ctx.author.id}):
					emb = discord.Embed(description = 'Вы не в клане!', timestamp = datetime.datetime.utcnow())
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

				elif not clan2.count_documents({"_id": member.id}):
					emb = discord.Embed(description = 'Пользователь не в клане!', timestamp = datetime.datetime.utcnow())
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)


				elif not clan.count_documents({"owner": ctx.author.id}):
					emb = discord.Embed(description = 'Только глава может отдать владельца клана!', timestamp = datetime.datetime.utcnow())
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

				else:
					clanName = clan2.find_one({"_id": ctx.author.id})['name']
					clanNameTwo = clan2.find_one({"_id": member.id})['name']

					if clanName == clanNameTwo:
						emb = discord.Embed(description = f'Вы успешно передали лидерство **{member}**', timestamp = datetime.datetime.utcnow())
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)

						clan.update_one({"name": clanName}, {"$set": {"owner": member.id}}) 

						clan2.update_one({"name": clanName}, {"$set": {"clanid": member.id}}) 

					else:
						emb = discord.Embed(description = 'Пользователь в другом клане!', timestamp = datetime.datetime.utcnow())
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def top(self, ctx, name = None):
		if ctx.channel.id == 668447958303506432 or ctx.channel.id == 730332130575384596:
			if name is None:
				emb = discord.Embed(description = 'Существующие топы: <member> <cash>', timestamp = datetime.datetime.utcnow())
				emb.set_author(icon_url = '{}'.format(ctx.author.avatar_url), name = '{}'.format(ctx.author))
				await ctx.send(embed = emb)

			else:
				if name.lower() == 'member':

					emb = discord.Embed(description = f':trophy: **[Топ 10 кланов по участникам:]({ctx.author.avatar_url})**')

					counter = 0
					for j in clan.find({"$query":{}, "$orderby":{"members":-1}}).limit(10):
						counter += 1

						if counter == 1:
							emb.add_field(
								name = f'[{counter}]    > :first_place: # {j["name"]}',
								value = f'| Участников: {j["members"]}',
								inline = False
							)
						elif counter == 2:
							emb.add_field(
								name = f'[{counter}]    > :second_place: # {j["name"]}',
								value = f'| Участников: {j["members"]}',
								inline = False
							)
						elif counter == 3:
							emb.add_field(
								name = f'[{counter}]    > :third_place: # {j["name"]}',
								value = f'| Участников: {j["members"]}',
								inline = False
							)
						else:

							emb.add_field(
								name = f'[{counter}]    > # {row[1]}',
								value = f'| Участников: {j["members"]}',
								inline = False
							)
					emb.set_author(name = f'Страница 1 из 1 — Всего учатников: {len(ctx.guild.members)}', icon_url = '{}'.format(ctx.guild.icon_url))
					await ctx.send(embed = emb)

				elif name.lower() == 'cash':
					emb = discord.Embed(description = f':trophy: **[Топ 10 кланов по балансу:]({ctx.author.avatar_url})**')

					counter = 0
					for j in clan.find({"$query":{}, "$orderby":{"cash":-1}}).limit(10):
						counter += 1

						if counter == 1:
							emb.add_field(
								name = f'[{counter}]    > :first_place: # {j["name"]}',
								value = f'| Баланс: <a:currency:737351940320657588> {j["cash"]}',
								inline = False
							)
						elif counter == 2:
							emb.add_field(
								name = f'[{counter}]    > :second_place: # {j["name"]}',
								value = f'| Баланс: <a:currency:737351940320657588> {j["cash"]}',
								inline = False
							)
						elif counter == 3:
							emb.add_field(
								name = f'[{counter}]    > :third_place: # {j["name"]}',
								value = f'| Баланс: <a:currency:737351940320657588> {j["cash"]}',
								inline = False
							)
						else:

							emb.add_field(
								name = f'[{counter}]    > # {j["name"]}',
								value = f'| Баланс: <a:currency:737351940320657588> {j["cash"]}',
								inline = False
							)
					emb.set_author(name = f'Страница 1 из 1 — Всего учатников: {len(ctx.guild.members)}', icon_url = '{}'.format(ctx.guild.icon_url))
					await ctx.send(embed = emb)
				else:
					emb = discord.Embed(description = 'Существующие топы: <member> <cash>', timestamp = datetime.datetime.utcnow())
					emb.set_author(icon_url = '{}'.format(ctx.author.avatar_url), name = '{}'.format(ctx.author))
					await ctx.send(embed = emb)
		
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def leave(self, ctx):
		if ctx.channel.id == 668447958303506432:

			if clan2.find_one({"_id": ctx.author.id})['name'] is None:
				
				emb = discord.Embed(description = 'Вы не в клане!', timestamp = datetime.datetime.utcnow())
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:

				if not clan.count_documents({"owner": ctx.author.id}):
					name = clan2.find_one({"_id": ctx.author.id})['name']

					emb = discord.Embed(description = f'Вы покинули клан {name}!', timestamp = datetime.datetime.utcnow())
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

					clan2.delete_one({"_id": ctx.author.id})

					for x in clan.find({"name": name}):
						members = x['members'] - 1
									
						clan.update_one({"name": name}, {"$set": {"members": members}}) 
			
				else:
					emb = discord.Embed(description = 'Глава не может покинуть клан!', timestamp = datetime.datetime.utcnow())
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def kick(self, ctx, member: discord.Member = None):
		if ctx.channel.id == 668447958303506432:

			if member is None:
				emb = discord.Embed(description = 'Укажите пользователя', timestamp = datetime.datetime.utcnow())
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			elif member == ctx.author:
				emb = discord.Embed(description = 'Самого себя кикнуть нельзя!', timestamp = datetime.datetime.utcnow())
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:

				if not clan2.count_documents({"_id": ctx.author.id}):
					
					emb = discord.Embed(description = 'Вы не в клане!', timestamp = datetime.datetime.utcnow())
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

				elif not clan2.count_documents({"_id": member.id}):
					
					emb = discord.Embed(description = 'Пользователь не в клане!', timestamp = datetime.datetime.utcnow())
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

				else:
					if not clan.count_documents({"owner": ctx.author.id}):

						emb = discord.Embed(description = 'Только глава может кикнуть участника с клана!', timestamp = datetime.datetime.utcnow())
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)

					else:
						clanName1 = clan2.find_one({"_id": ctx.author.id})['name']
						clanName2 = clan2.find_one({"_id": member.id})['name']

						if clanName1 == clanName2:
							emb = discord.Embed(description = 'Вы успешно кикнули участника с клана!', timestamp = datetime.datetime.utcnow())
							emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
							await ctx.send(embed = emb)

							name = clan2.find_one({"_id": ctx.author.id})['name']
							
							clan2.delete_one({"_id": member.id})

							for x in clan.find({"name": name}):
								members = x['members'] - 1
									
								clan.update_one({"name": name}, {"$set": {"members": members}}) 

						else:
							emb = discord.Embed(description = 'Данный человек находится в другом клане!', timestamp = datetime.datetime.utcnow())
							emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
							await ctx.send(embed = emb)
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def delete(self, ctx):
		if ctx.channel.id == 668447958303506432:

			if not clan2.count_documents({"_id": ctx.author.id}):
					
				emb = discord.Embed(description = 'Вы не в клане!', timestamp = datetime.datetime.utcnow())
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:
				if not clan.count_documents({"owner": ctx.author.id}):

					emb = discord.Embed(description = 'Только глава может удалить клан!', timestamp = datetime.datetime.utcnow())
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

				else:
					emb = discord.Embed(description = 'Вы успешно удалили клан!', timestamp = datetime.datetime.utcnow())
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

					name = clan2.find_one({"_id": ctx.author.id})['name']

					clan.delete_one({"name": name})

					for x in clan2.find({"name": name}):
						clan2.delete_one({"name": name})
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def award(self, ctx, amount: int = None):
		if ctx.channel.id == 668447958303506432 or ctx.channel.id == 730332130575384596:

			if amount is None:
				emb = discord.Embed(description = 'Укажите сумму!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			elif amount < 30:
				emb = discord.Embed(description = 'Сумма слишком маленькая!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:
				if not clan2.count_documents({"_id": ctx.author.id}):
					emb = discord.Embed(description = 'Вы не в клане!')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

				else:

					balance = db['test']

					if balance.find_one({"_id": ctx.author.id})['cash'] < amount:
						emb = discord.Embed(description = 'Сумма перевода больше суммы баланса!', timestamp = datetime.datetime.utcnow())
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)
					else:

						emb = discord.Embed(description = f'Вы успешно перевели в казну клана <a:currency:737351940320657588> {amount}', timestamp = datetime.datetime.utcnow())
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)

						name = clan2.find_one({"_id": ctx.author.id})['name']
											
						newcash1 = clan.find_one({"name": name})['cash'] + amount
						clan.update_one({"name": name}, {"$set": {"cash": newcash1}}) 
				
						newcash2 = balance.find_one({"_id": ctx.author.id})['cash'] - amount
						balance.update_one({"_id": ctx.author.id}, {"$set": {"cash": newcash2}}) 

		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def take(self, ctx, amount: int = None):
		if ctx.channel.id == 668447958303506432 or ctx.channel.id == 730332130575384596:

			if amount is None:
				emb = discord.Embed(description = 'Укажите сумму!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)
			else:
				if not clan.count_documents({"owner": ctx.author.id}):
					emb = discord.Embed(description = 'Только глава клана может взять деньги из клановой казны!', timestamp = datetime.datetime.utcnow())
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

				else:

					name = clan2.find_one({"_id": ctx.author.id})['name']

					cash = clan.find_one({"name": name})['cash']

					if cash < amount:
						emb = discord.Embed(description = 'Сумма перевода больше суммы баланса клановой казны!', timestamp = datetime.datetime.utcnow())
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)
					else:

						emb = discord.Embed(description = f'Вы успешно перевели себе <a:currency:737351940320657588> {amount}', timestamp = datetime.datetime.utcnow())
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)
						
						balance = db['test']

						newcash1 = clan.find_one({"name": name})['cash'] - amount
						clan.update_one({"name": name}, {"$set": {"cash": newcash1}}) 
				
						newcash2 = balance.find_one({"_id": ctx.author.id})['cash'] + amount
						balance.update_one({"_id": ctx.author.id}, {"$set": {"cash": newcash2}}) 
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def rename(self, ctx, *, name = None):
		if ctx.channel.id == 668447958303506432:

			if name is None:
				emb = discord.Embed(description = 'Введите название клана!', timestamp = datetime.datetime.utcnow())
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			elif len(name) > 25:
				emb = discord.Embed(description = 'Имя клана слишком длиное!', timestamp = datetime.datetime.utcnow())
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:
					
				if not clan2.count_documents({"_id": ctx.author.id}):
					emb = discord.Embed(description = 'Вы не в клане!')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)
				else:
					if not clan.count_documents({"owner": ctx.author.id}):
						emb = discord.Embed(description = 'Только глава может изменить имя клана!', timestamp = datetime.datetime.utcnow())
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)

					else:
						if clan.count_documents({"name": name}):
							emb = discord.Embed(description = 'Такой клан уже существует!', timestamp = datetime.datetime.utcnow())
							emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
							await ctx.send(embed = emb)
						else:

							balance = db['test']
							result = balance.find_one({"_id": ctx.author.id})['cash']
							if result > 4000:
								emb = discord.Embed(description = f'Вы изменили имя клана на **{name}**', timestamp = datetime.datetime.utcnow())
								emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
								
								await ctx.send(embed = emb)
								
								names = clan2.find_one({"_id": ctx.author.id})['name']
								clan.update_one({"name": names}, {"$set": {"name": name}}) 
								for x in clan2.find({"name": names}):
									clan2.update_one({"name": names}, {"$set": {"name": name}}) 

								newcash2 = balance.find_one({"_id": ctx.author.id})['cash'] - 4000
								balance.update_one({"_id": ctx.author.id}, {"$set": {"cash": newcash2}}) 

							else:
								emb = discord.Embed(description = 'Недостаточно денег!', timestamp = datetime.datetime.utcnow())
								emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
								await ctx.send(embed = emb)
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

def setup(Bot):
	Bot.add_cog(Clans(Bot))
	print('[INFO] Clans загружен!')

