@client.group()
async def clan(ctx):
	pass


@clan.command()
async def buy(ctx, link = None, *, name = None):
	if name is None:
		emb = discord.Embed(description = 'Введите название клана!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

		await ctx.message.delete()

	elif link is None:
		emb = discord.Embed(description = 'Укажите ссылку на баннер для клана!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

		await ctx.message.delete()

	elif len(name) > 25:
		emb = discord.Embed(description = 'Имя клана слишком длиное!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

		await ctx.message.delete()

	else:
		cursor.execute("SELECT cash FROM test24 WHERE id = {}".format(ctx.author.id))
		result = cursor.fetchone()[0]

		if result < 30000:
			emb = discord.Embed(description = 'У вас недостаточно денег!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

			await ctx.message.delete()

		else:
	
			person = cursor.execute("SELECT clanName FROM clanInvite19 WHERE id = {}".format(ctx.author.id)).fetchone() 

			if person is None:
				
				cursor.execute("UPDATE test24 SET cash = cash - {} WHERE id = {}".format(30000, ctx.author.id))
				connection.commit()

				cursor.execute("INSERT INTO clanOwners10 VALUES ({}, '{}', '{}', {}, '{}')".format(ctx.author.id, name, 'Пусто', 1, link))
				connection.commit()

				cursor.execute("INSERT INTO clanInvite19 VALUES ({}, '{}', {})".format(ctx.author.id, name, ctx.author.id))
				connection.commit()

				emb = discord.Embed(description = 'Вы успешно создали клан!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

				await ctx.message.delete()

			else:
				clanName = cursor.execute("SELECT clanName FROM clanInvite19 WHERE id = {}".format(ctx.author.id)).fetchone()[0]

				emb = discord.Embed(description = f'Вы уже в клане {clanName}')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

				await ctx.message.delete()


@clan.command()
async def info(ctx, *, name = None):
	if name is None:
		emb = discord.Embed(description = 'Введите название клана!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

	else:

		message = await ctx.send('Обработка... Если ответа не последует, указано неверное имя клана или у клана нет баннера!')
		try:
			for row in cursor.execute("SELECT clanName, clanId FROM clanInvite19"):
			
				if name == row[0]:

					banner = cursor.execute("SELECT banner FROM clanOwners10 WHERE clanName = '{}'".format(row[0])).fetchone()[0]

					bio = cursor.execute("SELECT bio FROM clanOwners10 WHERE clanName = '{}'".format(row[0])).fetchone()[0]
					members = cursor.execute("SELECT members FROM clanOwners10 WHERE clanName = '{}'".format(row[0])).fetchone()[0]

					emb = discord.Embed(title = f'Клан {row[0]}', description = f'```fix\nОписание: {bio}```')
					
					emb.add_field(name = 'Владелец:', value = f'```diff\n- {client.get_user(row[1])}```')
					emb.add_field(name = 'Участников:', value = f'```diff\n- {members}```')

					try:
						emb.set_thumbnail(url = banner)
					except:
						pass

					await ctx.send(embed = emb)
					await message.delete()

				else:
					pass
		except:
			pass

@clan.command()
async def banner(ctx, link = None):
	if link is None:
		emb = discord.Embed(description = 'Укажите ссылку на баннер для клана!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

	else:
		try:
			if cursor.execute("SELECT owner FROM clanOwners10 WHERE owner = {}".format(ctx.author.id)).fetchone() != None:

				name = cursor.execute("SELECT clanName FROM clanOwners10 WHERE owner = {}".format(ctx.author.id)).fetchone()[0]
				
				cursor.execute("UPDATE clanOwners10 SET banner = '{}' WHERE clanName = '{}'".format(link, name))
				connection.commit()

				
				emb = discord.Embed(description = 'Вы поменяли баннер клана!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))

				emb.set_image(url = link)

				await ctx.send(embed = emb)
				await ctx.message.delete()
			else:
				emb = discord.Embed(description = 'Только глава может поменять баннер клана!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

				await ctx.message.delete()		
		except:
			pass

@clan.command()
async def bio(ctx, *, name = None):
		
	if cursor.execute("SELECT owner FROM clanOwners10 WHERE owner = {}".format(ctx.author.id)).fetchone() != None:

		if name is None:
			emb = discord.Embed(description = 'Укажите описание!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

		else:
			clanName = cursor.execute("SELECT clanName FROM clanOwners10 WHERE owner = {}".format(ctx.author.id)).fetchone()[0]

			cursor.execute("UPDATE clanOwners10 SET bio = '{}' WHERE clanName = '{}'".format(name, clanName))
			connection.commit()

			emb = discord.Embed(description = f'Вы поменяли описание вашего клана на:\n```fix\n{name}```')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)
	
	else:
		emb = discord.Embed(description = 'Только глава может поменять описание клана!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

@clan.command()
async def invite(ctx, member: discord.Member = None):
	if member is None:
		emb = discord.Embed(description = 'Укажите пользователя!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

	else:
		if cursor.execute("SELECT owner FROM clanOwners10 WHERE owner = {}".format(ctx.author.id)).fetchone() != None:
			name = cursor.execute("SELECT clanName FROM clanInvite19 WHERE id = {}".format(ctx.author.id)).fetchone()[0]

			if cursor.execute("SELECT clanName FROM clanInvite19 WHERE id = {}".format(member.id)).fetchone() is None:
					
				solutions = ['✅', '❌']
				emb = discord.Embed(description = f'{member} хотите ли вы вступить в клан {name}?')
					
				message = await ctx.send(embed = emb)
					
				for x in solutions:
					await message.add_reaction(x)

				try:
					react, user = await client.wait_for('reaction_add', timeout= 30.0, check= lambda react, user: user == member and react.message.channel == ctx.channel and react.emoji in solutions)
				except asyncio.TimeoutError:
					emb = discord.Embed(description = 'Время на ответ вышло')
					emb.set_author(icon_url = '{}'.format(ctx.author.avatar_url), name = '{}'.format(ctx.author))

					await message.edit(embed = emb)
					await message.clear_reactions()
				else:
					if str(react.emoji) == '✅':
						await message.clear_reactions()

						cursor.execute("INSERT INTO clanInvite19 VALUES ({}, '{}', {})".format(member.id, name, ctx.author.id))
						connection.commit()

						cursor.execute("UPDATE clanOwners10 SET members = members + {} WHERE clanName = '{}'".format(1, name))
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


@clan.command()
async def top(ctx):
	emb = discord.Embed(title = f'Топ 10 кланов по участникам {ctx.guild.name}')

	for row in cursor.execute("SELECT * FROM clanOwners10 ORDER BY members DESC LIMIT 10"):
		emb.add_field(
				name = f'Клан: {row[1]}',
				value = f'Участников: {row[3]}',
				inline = False
			)

	await ctx.send(embed = emb)

@clan.command()
async def leave(ctx):
	if cursor.execute("SELECT clanName FROM clanInvite19 WHERE id = {}".format(ctx.author.id)).fetchone() is None:
		
		emb = discord.Embed(description = 'Вы не в клане!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

	else:

		if cursor.execute("SELECT owner FROM clanOwners10 WHERE owner = {}".format(ctx.author.id)).fetchone() is None:
			name = cursor.execute("SELECT clanName FROM clanInvite19 WHERE id = {}".format(ctx.author.id)).fetchone()[0]

			emb = discord.Embed(description = f'Вы покинули клан {name}!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

			cursor.execute("DELETE FROM clanInvite19 WHERE id = {}".format(ctx.author.id))
			connection.commit()

			cursor.execute("UPDATE clanOwners10 SET members = members - {} WHERE clanName = '{}'".format(1, name))
			connection.commit()

			
		else:
			emb = discord.Embed(description = 'Глава не может покинуть клан!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

@clan.command()
async def kick(ctx, member: discord.Member = None):
	if member is None:
		emb = discord.Embed(description = 'Укажите пользователя')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

	elif member == ctx.author:
		emb = discord.Embed(description = 'Самого себя кикнуть нельзя!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

	else:

		if cursor.execute("SELECT clanName FROM clanInvite19 WHERE id = {}".format(ctx.author.id)).fetchone() is None:
			
			emb = discord.Embed(description = 'Вы не в клане!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

		elif cursor.execute("SELECT clanName FROM clanInvite19 WHERE id = {}".format(member.id)).fetchone() is None:
			
			emb = discord.Embed(description = 'Пользователь не в клане!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

		else:
			if cursor.execute("SELECT owner FROM clanOwners10 WHERE owner = {}".format(ctx.author.id)).fetchone() is None:

				emb = discord.Embed(description = 'Только глава может кикнуть участника с клана!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:
				clanName = cursor.execute("SELECT clanName FROM clanInvite19 WHERE id = {}".format(ctx.author.id)).fetchone()
				clanNameTwo = cursor.execute("SELECT clanName FROM clanInvite19 WHERE id = {}".format(member.id)).fetchone()

				if clanName == clanNameTwo:
					name = cursor.execute("SELECT clanName FROM clanInvite19 WHERE id = {}".format(ctx.author.id)).fetchone()[0]
					
					cursor.execute("DELETE FROM clanInvite19 WHERE id = {}".format(member.id))
					connection.commit()

					cursor.execute("UPDATE clanOwners10 SET members = members - {} WHERE clanName = '{}'".format(1, name))
					connection.commit()

					emb = discord.Embed(description = 'Вы успешно кикнули участника с клана!')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

				else:
					emb = discord.Embed(description = 'Данный человек находится в другом клане!')
					emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
					await ctx.send(embed = emb)

@clan.command()
async def delete(ctx):
	if cursor.execute("SELECT clanName FROM clanInvite19 WHERE id = {}".format(ctx.author.id)).fetchone() is None:
			
		emb = discord.Embed(description = 'Вы не в клане!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

	else:
		if cursor.execute("SELECT owner FROM clanOwners10 WHERE owner = {}".format(ctx.author.id)).fetchone() is None:

			emb = discord.Embed(description = 'Только глава может удалить клан!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

		else:
			name = cursor.execute("SELECT clanName FROM clanInvite19 WHERE id = {}".format(ctx.author.id)).fetchone()[0]
			nameTwo = cursor.execute("SELECT clanName FROM clanOwners10 WHERE owner = {}".format(ctx.author.id)).fetchone()[0]


			cursor.execute("DELETE FROM clanInvite19 WHERE clanName = '{}'".format(name))
			connection.commit()

			cursor.execute("DELETE FROM clanOwners10 WHERE clanName = '{}'".format(nameTwo))
			connection.commit()

			emb = discord.Embed(description = 'Вы успешно удалили клан!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))

