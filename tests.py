class Clans(commands.Cog):
	def __init__(self, Bot):
		self.Bot = Bot


	cursor.execute("""CREATE TABLE IF NOT EXISTS clanInvite26(
		id INT,
		clanName TEXT,
		clanId INT
	)""")

	cursor.execute("""CREATE TABLE IF NOT EXISTS clanOwners15(
		owner INT,
		clanName TEXT,
		bio TEXT,
		members INT,
		banner TEXT,
		cash INT,
		datem TEXT
	)""")

	connection.commit()

	@commands.group()
	async def clan(self, ctx):
		pass


	@clan.command()
	async def buy(self, ctx, *, name = None):
		if ctx.channel.id == 730332130575384596:

			if name is None:
				emb = discord.Embed(description = 'Введите название клана!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

				await ctx.message.delete()

			elif len(name) > 25:
				emb = discord.Embed(description = 'Имя клана слишком длиное!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

				await ctx.message.delete()

			else:
				cursor.execute("SELECT cash FROM flw6 WHERE id = {}".format(ctx.author.id))
				result = cursor.fetchone()[0]

				if result < 30000:
					emb = discord.Embed(description = 'У вас недостаточно денег!')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

					await ctx.message.delete()

				else:
					
					clans = []
					for names in cursor.execute("SELECT clanName FROM clanInvite26"):
						if name == names[0]:
							clans.append(names[0])
						else:
							pass

					if name in clans:
						emb = discord.Embed(description = 'Такой клан уже существует!')
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)

						await ctx.message.delete()

					else:

						person = cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone() 

						if person is None:
							
							cursor.execute("UPDATE flw6 SET cash = cash - {} WHERE id = {}".format(30000, ctx.author.id))
							connection.commit()

							cursor.execute("INSERT INTO clanOwners15 VALUES ({}, '{}', '{}', {}, '{}', {}, '{}')".format(ctx.author.id, name, 'Пусто', 1, None, 0, datetime.datetime.today()))
							connection.commit()

							cursor.execute("INSERT INTO clanInvite26 VALUES ({}, '{}', {})".format(ctx.author.id, name, ctx.author.id))
							connection.commit()

							emb = discord.Embed(description = 'Вы успешно создали клан!')
							emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
							await ctx.send(embed = emb)

							await ctx.message.delete()

						else:
							clanName = cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone()[0]

							emb = discord.Embed(description = f'Вы уже в клане {clanName}')
							emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
							await ctx.send(embed = emb)

							await ctx.message.delete()
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

				message = await ctx.send('Обработка... Если ответа не последует, указано неверное имя клана или у клана нет баннера!')
				try:
					for row in cursor.execute("SELECT clanName, clanId FROM clanInvite26"):
					
						if name == row[0]:
							cash = cursor.execute("SELECT cash FROM clanOwners15 WHERE clanName = '{}'".format(row[0])).fetchone()[0]
							
							banner = cursor.execute("SELECT banner FROM clanOwners15 WHERE clanName = '{}'".format(row[0])).fetchone()[0]
							date = cursor.execute("SELECT datem FROM clanOwners15 WHERE clanName = '{}'".format(row[0])).fetchone()[0]

							bio = cursor.execute("SELECT bio FROM clanOwners15 WHERE clanName = '{}'".format(row[0])).fetchone()[0]
							members = cursor.execute("SELECT members FROM clanOwners15 WHERE clanName = '{}'".format(row[0])).fetchone()[0]

							emb = discord.Embed(description = f'**[Информация клана | {row[0]}]({ctx.author.avatar_url})**\n```fix\nОписание: {bio}```')
							
							emb.add_field(name = 'Владелец:', value = f'```diff\n- {self.Bot.get_user(row[1])}```')
							emb.add_field(name = 'Участников:', value = f'```diff\n- {members}```')
							emb.add_field(name = 'Казна клана:', value = f'```diff\n- {cash}```')

							emb.add_field(name = 'Дата создания:', value = f'```md\n#{date}```')


							emb.set_thumbnail(url = banner)

							await ctx.send(embed = emb)
							await message.delete()

						else:
							pass
				except:
					for row in cursor.execute("SELECT clanName, clanId FROM clanInvite26"):
					
						if name == row[0]:
							cash = cursor.execute("SELECT cash FROM clanOwners15 WHERE clanName = '{}'".format(row[0])).fetchone()[0]
							
							banner = cursor.execute("SELECT banner FROM clanOwners15 WHERE clanName = '{}'".format(row[0])).fetchone()[0]
							date = cursor.execute("SELECT datem FROM clanOwners15 WHERE clanName = '{}'".format(row[0])).fetchone()[0]

							bio = cursor.execute("SELECT bio FROM clanOwners15 WHERE clanName = '{}'".format(row[0])).fetchone()[0]
							members = cursor.execute("SELECT members FROM clanOwners15 WHERE clanName = '{}'".format(row[0])).fetchone()[0]

							emb = discord.Embed(description = f'**[Информация клана | {row[0]}]({ctx.author.avatar_url})**\n```fix\nОписание: {bio}```')
							
							emb.add_field(name = 'Владелец:', value = f'```diff\n- {self.Bot.get_user(row[1])}```')
							emb.add_field(name = 'Участников:', value = f'```diff\n- {members}```')
							emb.add_field(name = 'Казна клана:', value = f'```diff\n- 💎 {cash}```')

							emb.add_field(name = 'Дата создания:', value = f'```md\n#{date}```')


							await ctx.send(embed = emb)
							await message.delete()

						else:
							pass
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def banner(self, ctx, link = None):
		if ctx.channel.id == 668447958303506432:

			if link is None:
				emb = discord.Embed(description = 'Укажите ссылку на баннер для клана!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:				
				try:
					if cursor.execute("SELECT owner FROM clanOwners15 WHERE owner = {}".format(ctx.author.id)).fetchone() != None:
						cursor.execute("SELECT cash FROM flw6 WHERE id = {}".format(ctx.author.id))
						result = cursor.fetchone()[0]

						if result > 5000:

							name = cursor.execute("SELECT clanName FROM clanOwners15 WHERE owner = {}".format(ctx.author.id)).fetchone()[0]
								
							cursor.execute("UPDATE clanOwners15 SET banner = '{}' WHERE clanName = '{}'".format(link, name))
							connection.commit()

							cursor.execute("UPDATE flw6 SET cash = cash - {} WHERE id = {}".format(5000, ctx.author.id))
							connection.commit()
								
							emb = discord.Embed(description = 'Вы поменяли баннер клана!')
							emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))

							emb.set_image(url = link)

							await ctx.send(embed = emb)
							await ctx.message.delete()
							
						else:
								
							emb = discord.Embed(description = 'Недостаточно денег!')
							emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
							await ctx.send(embed = emb)
					else:
						emb = discord.Embed(description = 'Только глава может поменять баннер клана!')
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)

						await ctx.message.delete()		
				except:
					await ctx.send('Нужно указать **ссылку** на картинку для баннера!')
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def bio(self, ctx, *, name = None):
		if ctx.channel.id == 668447958303506432:	
			if cursor.execute("SELECT owner FROM clanOwners15 WHERE owner = {}".format(ctx.author.id)).fetchone() != None:

				if name is None:
					emb = discord.Embed(description = 'Укажите описание!')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

				else:
					clanName = cursor.execute("SELECT clanName FROM clanOwners15 WHERE owner = {}".format(ctx.author.id)).fetchone()[0]

					cursor.execute("UPDATE clanOwners15 SET bio = '{}' WHERE clanName = '{}'".format(name, clanName))
					connection.commit()

					emb = discord.Embed(description = f'Вы поменяли описание вашего клана на:\n```fix\n{name}```')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)
			
			else:
				emb = discord.Embed(description = 'Только глава может поменять описание клана!')
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
				emb = discord.Embed(description = 'Укажите пользователя!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:
				if cursor.execute("SELECT owner FROM clanOwners15 WHERE owner = {}".format(ctx.author.id)).fetchone() != None:
					name = cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone()[0]

					if cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(member.id)).fetchone() is None:
							
						solutions = ['✅', '❌']
						emb = discord.Embed(description = f'{member} хотите ли вы вступить в клан {name}?')
							
						message = await ctx.send(embed = emb)
							
						for x in solutions:
							await message.add_reaction(x)

						try:
							react, user = await self.Bot.wait_for('reaction_add', timeout= 30.0, check= lambda react, user: user == member and react.message.channel == ctx.channel and react.emoji in solutions)
						except asyncio.TimeoutError:
							emb = discord.Embed(description = 'Время на ответ вышло')
							emb.set_author(icon_url = '{}'.format(ctx.author.avatar_url), name = '{}'.format(ctx.author))

							await message.edit(embed = emb)
							await message.clear_reactions()
						else:
							if str(react.emoji) == '✅':
								await message.clear_reactions()

								cursor.execute("INSERT INTO clanInvite26 VALUES ({}, '{}', {})".format(member.id, name, ctx.author.id))
								connection.commit()

								cursor.execute("UPDATE clanOwners15 SET members = members + {} WHERE clanName = '{}'".format(1, name))
								connection.commit()
										
								emb = discord.Embed(description = f'{member} вступил в клан {name}!')
								emb.set_author(icon_url = '{}'.format(ctx.author.avatar_url), name = '{}'.format(ctx.author))
								await message.edit(embed = emb)
									
							elif str(react.emoji) == '❌':
								await message.clear_reactions()

								emb = discord.Embed(description = f'{member} отказался от приглашения!')
								emb.set_author(icon_url = '{}'.format(ctx.author.avatar_url), name = '{}'.format(ctx.author))

								await message.edit(embed = emb)

					else:

						emb = discord.Embed(description = 'Пользователь уже в клане!')
						emb.set_author(icon_url = '{}'.format(ctx.author.avatar_url), name = '{}'.format(ctx.author))
						await ctx.send(embed = emb)
				else:

					emb = discord.Embed(description = 'Только глава может приглашать людей!')
					emb.set_author(icon_url = '{}'.format(ctx.author.avatar_url), name = '{}'.format(ctx.author))
					await ctx.send(embed = emb)
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()


	@clan.command()
	async def top(self, ctx, name = None):
		if ctx.channel.id == 668447958303506432:
			if name is None:
				emb = discord.Embed(description = 'Существующие топы: <member> <cash>')
				emb.set_author(icon_url = '{}'.format(ctx.author.avatar_url), name = '{}'.format(ctx.author))
				await ctx.send(embed = emb)

			else:
				if name.lower() == 'member':

					emb = discord.Embed(description = f':trophy: **[Топ 10 кланов по участникам:]({ctx.author.avatar_url})**')

					counter = 0
					for row in cursor.execute("SELECT * FROM clanOwners15 ORDER BY members DESC LIMIT 10"):
						counter += 1

						if counter == 1:
								emb.add_field(
									name = f'[{counter}]    > :first_place: # {row[1]}',
									value = f'| Участников: {row[3]}',
									inline = False
								)
						elif counter == 2:
							emb.add_field(
								name = f'[{counter}]    > :second_place: # {row[1]}',
								value = f'| Участников: {row[3]}',
								inline = False
							)
						elif counter == 3:
							emb.add_field(
								name = f'[{counter}]    > :third_place: # {row[1]}',
								value = f'| Участников: {row[3]}',
								inline = False
							)
						else:

							emb.add_field(
								name = f'[{counter}]    > # {row[1]}',
								value = f'| Участников: {row[3]}',
								inline = False
							)
					emb.set_author(name = f'Страница 1 из 1 — Всего учатников: {len(ctx.guild.members)}', icon_url = '{}'.format(ctx.guild.icon_url))
					await ctx.send(embed = emb)

				elif name.lower() == 'cash':
					emb = discord.Embed(description = f':trophy: **[Топ 10 кланов по балансу:]({ctx.author.avatar_url})**')

					counter = 0
					for row in cursor.execute("SELECT * FROM clanOwners15 ORDER BY cash DESC LIMIT 10"):
						counter += 1

						if counter == 1:
								emb.add_field(
									name = f'[{counter}]    > :first_place: # {row[1]}',
									value = f'| Баланс: <a:currency:737351940320657588> {row[5]}',
									inline = False
								)
						elif counter == 2:
							emb.add_field(
								name = f'[{counter}]    > :second_place: # {row[1]}',
								value = f'| Баланс: <a:currency:737351940320657588> {row[5]}',
								inline = False
							)
						elif counter == 3:
							emb.add_field(
								name = f'[{counter}]    > :third_place: # {row[1]}',
								value = f'| Баланс: <a:currency:737351940320657588> {row[5]}',
								inline = False
							)
						else:

							emb.add_field(
								name = f'[{counter}]    > # {row[1]}',
								value = f'| Баланс: <a:currency:737351940320657588> {row[5]}',
								inline = False
							)
					emb.set_author(name = f'Страница 1 из 1 — Всего учатников: {len(ctx.guild.members)}', icon_url = '{}'.format(ctx.guild.icon_url))
					await ctx.send(embed = emb)
		
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def leave(self, ctx):
		if ctx.channel.id == 668447958303506432:

			if cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone() is None:
				
				emb = discord.Embed(description = 'Вы не в клане!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:

				if cursor.execute("SELECT owner FROM clanOwners15 WHERE owner = {}".format(ctx.author.id)).fetchone() is None:
					name = cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone()[0]

					emb = discord.Embed(description = f'Вы покинули клан {name}!')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

					cursor.execute("DELETE FROM clanInvite26 WHERE id = {}".format(ctx.author.id))
					connection.commit()

					cursor.execute("UPDATE clanOwners15 SET members = members - {} WHERE clanName = '{}'".format(1, name))
					connection.commit()

					
				else:
					emb = discord.Embed(description = 'Глава не может покинуть клан!')
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
				emb = discord.Embed(description = 'Укажите пользователя')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			elif member == ctx.author:
				emb = discord.Embed(description = 'Самого себя кикнуть нельзя!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:

				if cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone() is None:
					
					emb = discord.Embed(description = 'Вы не в клане!')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

				elif cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(member.id)).fetchone() is None:
					
					emb = discord.Embed(description = 'Пользователь не в клане!')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

				else:
					if cursor.execute("SELECT owner FROM clanOwners15 WHERE owner = {}".format(ctx.author.id)).fetchone() is None:

						emb = discord.Embed(description = 'Только глава может кикнуть участника с клана!')
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)

					else:
						clanName = cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone()
						clanNameTwo = cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(member.id)).fetchone()

						if clanName == clanNameTwo:
							name = cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone()[0]
							
							cursor.execute("DELETE FROM clanInvite26 WHERE id = {}".format(member.id))
							connection.commit()

							cursor.execute("UPDATE clanOwners15 SET members = members - {} WHERE clanName = '{}'".format(1, name))
							connection.commit()

							emb = discord.Embed(description = 'Вы успешно кикнули участника с клана!')
							emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
							await ctx.send(embed = emb)

						else:
							emb = discord.Embed(description = 'Данный человек находится в другом клане!')
							emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
							await ctx.send(embed = emb)
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def delete(self, ctx):
		if ctx.channel.id == 668447958303506432:

			if cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone() is None:
					
				emb = discord.Embed(description = 'Вы не в клане!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:
				if cursor.execute("SELECT owner FROM clanInvite26 WHERE owner = {}".format(ctx.author.id)).fetchone() is None:

					emb = discord.Embed(description = 'Только глава может удалить клан!')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

				else:
					name = cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone()[0]
					nameTwo = cursor.execute("SELECT clanName FROM clanOwners15 WHERE owner = {}".format(ctx.author.id)).fetchone()[0]


					cursor.execute("DELETE FROM clanInvite26 WHERE clanName = '{}'".format(name))
					connection.commit()

					cursor.execute("DELETE FROM clanOwners15 WHERE clanName = '{}'".format(nameTwo))
					connection.commit()

					emb = discord.Embed(description = 'Вы успешно удалили клан!')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)
		else:
			await ctx.message.add_reaction('❌')

			await asyncio.sleep(5)
			await ctx.message.delete()

	@clan.command()
	async def award(self, ctx, amount: int = None):
		if amount is None:
			emb = discord.Embed(description = 'Укажите сумму!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)
		else:
			if cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone() is None:
				emb = discord.Embed(description = 'Вы не в клане!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:

				cursor.execute("SELECT cash FROM flw6 WHERE id = {}".format(ctx.author.id))
				result = cursor.fetchone()[0]

				if result < amount:
					emb = discord.Embed(description = 'Сумма перевода больше суммы баланса!')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)
				else:

					emb = discord.Embed(description = f'Вы успешно перевели <a:currency:737351940320657588> {amount} вашему клану!')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

					name = cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone()[0]
					
					cursor.execute("UPDATE clanOwners15 SET cash = cash + {} WHERE clanName = '{}'".format(amount, name))
					connection.commit()

					cursor.execute("UPDATE flw6 SET cash = cash - {} WHERE id = {}".format(amount, ctx.author.id))
					connection.commit()

	@clan.command()
	async def take(self, ctx, amount: int = None):
		if amount is None:
			emb = discord.Embed(description = 'Укажите сумму!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)
		else:
			if cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone() is None:
				emb = discord.Embed(description = 'Вы не в клане!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:

				name = cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone()[0]

				cursor.execute("SELECT cash FROM clanOwners15 WHERE clanName = '{}'".format(name))
				result = cursor.fetchone()[0]

				if result < amount:
					emb = discord.Embed(description = 'Сумма перевода больше суммы баланса клана!')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)
				else:

					emb = discord.Embed(description = f'Вы успешно перевели себе <a:currency:737351940320657588> {amount}')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)
					
					cursor.execute("UPDATE clanOwners15 SET cash = cash - {} WHERE clanName = '{}'".format(amount, name))
					connection.commit()

					cursor.execute("UPDATE flw6 SET cash = cash + {} WHERE id = {}".format(amount, ctx.author.id))
					connection.commit()

	@clan.command()
	async def rename(self, ctx, *, name = None):
		if name is None:
			emb = discord.Embed(description = 'Введите название клана!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

		elif len(name) > 25:
			emb = discord.Embed(description = 'Имя клана слишком длиное!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

		else:
				
			if cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone() is None:
				emb = discord.Embed(description = 'Вы не в клане!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)
			else:
				if cursor.execute("SELECT owner FROM clanOwners15 WHERE owner = {}".format(ctx.author.id)).fetchone() is None:
					emb = discord.Embed(description = 'Только глава может изменить имя клана!')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

				else:
					clans = []
					for clanNames in cursor.execute("SELECT clanName FROM clanInvite26"):
						if name == clanNames[0]:
							clans.append(clanNames[0])
						else:
							pass

					if name in clans:
						emb = discord.Embed(description = 'Такой клан уже существует!')
						emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
						await ctx.send(embed = emb)
					else:

						cursor.execute("SELECT cash FROM flw6 WHERE id = {}".format(ctx.author.id))
						result = cursor.fetchone()[0]

						if result > 3000:

							names = cursor.execute("SELECT clanName FROM clanInvite26 WHERE id = {}".format(ctx.author.id)).fetchone()[0]

							cursor.execute("UPDATE clanInvite26 SET clanName = '{}' WHERE clanName = '{}'".format(name, names))
							connection.commit()

							cursor.execute("UPDATE clanOwners15 SET clanName = '{}' WHERE clanName = '{}'".format(name, names))
							connection.commit()

							emb = discord.Embed(description = f'Вы изменили имя клана на {name}')
							emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
							await ctx.send(embed = emb)
						else:
							emb = discord.Embed(description = 'Недостаточно денег!')
							emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
							await ctx.send(embed = emb)

def setup(Bot):
	Bot.add_cog(Clans(Bot))
	print('[INFO] Clans загружен!')

