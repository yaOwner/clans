@client.group()
async def clan(ctx):
	pass


@clan.command()
async def buy(ctx, *, name = None):
	if name is None:
		emb = discord.Embed(description = 'Введите название клана!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

	elif len(name) > 25:
		emb = discord.Embed(description = 'Имя клана слишком длиное!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

	else:
		cursor.execute("SELECT cash FROM test24 WHERE id = {}".format(ctx.author.id))
		result = cursor.fetchone()[0]

		if result < 30000:
			emb = discord.Embed(description = 'У вас недостаточно денег!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

		else:
	
			person = cursor.execute("SELECT clanName FROM clanInvite17 WHERE id = {}".format(ctx.author.id)).fetchone() 

			if person is None:
				
				cursor.execute("UPDATE test24 SET cash = cash - {} WHERE id = {}".format(30000, ctx.author.id))
				connection.commit()

				cursor.execute("INSERT INTO clanOwners6 VALUES ({}, '{}', '{}', {})".format(ctx.author.id, name, 'Пусто', 1))
				connection.commit()

				cursor.execute("INSERT INTO clanInvite17 VALUES ({}, '{}', {})".format(ctx.author.id, name, ctx.author.id))
				connection.commit()

				emb = discord.Embed(description = 'Вы успешно создали клан!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:
				clanName = cursor.execute("SELECT clanName FROM clanInvite17 WHERE id = {}".format(ctx.author.id)).fetchone()[0]

				emb = discord.Embed(description = f'Вы уже в клане {clanName}')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)


@clan.command()
async def info(ctx, *, name = None):
	if name is None:
		emb = discord.Embed(description = 'Введите название клана!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

	else:
		message = await ctx.send('Обработка... Если ответа не последует, указано неверное имя клана')

		for row in cursor.execute("SELECT clanName, clanId FROM clanInvite17"):
		
			if name == row[0]:
				await message.delete()

				bio = cursor.execute("SELECT bio FROM clanOwners6 WHERE clanName = '{}'".format(row[0])).fetchone()[0]
				members = cursor.execute("SELECT members FROM clanOwners6 WHERE clanName = '{}'".format(row[0])).fetchone()[0]

				emb = discord.Embed(title = f'Клан {row[0]}', description = f'```fix\nОписание: {bio}```')
				
				emb.add_field(name = 'Владелец:', value = f'```diff\n- {client.get_user(row[1])}```')
				emb.add_field(name = 'Участников:', value = f'```diff\n- {members}```')

				await ctx.send(embed = emb)

			else:
				pass

@clan.command()
async def bio(ctx, *, name = None):
		
	if cursor.execute("SELECT owner FROM clanOwners6 WHERE owner = {}".format(ctx.author.id)).fetchone() != None:

		if name is None:
			emb = discord.Embed(description = 'Укажите описание!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

		else:
			clanName = cursor.execute("SELECT clanName FROM clanOwners6 WHERE owner = {}".format(ctx.author.id)).fetchone()[0]

			cursor.execute("UPDATE clanOwners6 SET bio = '{}' WHERE clanName = '{}'".format(name, clanName))
			connection.commit()

			emb = discord.Embed(description = f'Вы поменяли описание вашего клана на:\n```fix\n{name}```')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)
	
	else:
		emb = discord.Embed(description = 'Только глава клана может поменять описание клана!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

@clan.command()
async def invite(ctx, member: discord.Member = None):
	if member is None:
		emb = discord.Embed(description = 'Укажите пользователя!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

	else:
		if cursor.execute("SELECT owner FROM clanOwners6 WHERE owner = {}".format(ctx.author.id)).fetchone() != None:
			name = cursor.execute("SELECT clanName FROM clanInvite17 WHERE id = {}".format(ctx.author.id)).fetchone()[0]

			if cursor.execute("SELECT clanName FROM clanInvite17 WHERE id = {}".format(member.id)).fetchone() is None:
					
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

						cursor.execute("INSERT INTO clanInvite17 VALUES ({}, '{}', {})".format(member.id, name, ctx.author.id))
						connection.commit()

						cursor.execute("UPDATE clanOwners6 SET members = members + {} WHERE clanName = '{}'".format(1, name))
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

	for row in cursor.execute("SELECT * FROM clanOwners6 ORDER BY members DESC LIMIT 10"):
		emb.add_field(
				name = f'Клан: {row[1]}',
				value = f'Участников: {row[3]}',
				inline = False
			)

	await ctx.send(embed = emb)

@clan.command()
async def leave(ctx):
	if cursor.execute("SELECT clanName FROM clanInvite17 WHERE id = {}".format(ctx.author.id)).fetchone() is None:
		
		emb = discord.Embed(description = 'Вы не в клане!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

	else:

		if cursor.execute("SELECT owner FROM clanOwners6 WHERE owner = {}".format(ctx.author.id)).fetchone() is None:
			name = cursor.execute("SELECT clanName FROM clanInvite17 WHERE id = {}".format(ctx.author.id)).fetchone()[0]

			emb = discord.Embed(description = f'Вы покинули клан {name}!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

			cursor.execute("DELETE FROM clanInvite17 WHERE id = {}".format(ctx.author.id))
			connection.commit()

			cursor.execute("UPDATE clanOwners6 SET members = members - {} WHERE clanName = '{}'".format(1, name))
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

		if cursor.execute("SELECT clanName FROM clanInvite17 WHERE id = {}".format(ctx.author.id)).fetchone() is None:
			
			emb = discord.Embed(description = 'Вы не в клане!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

		elif cursor.execute("SELECT clanName FROM clanInvite17 WHERE id = {}".format(member.id)).fetchone() is None:
			
			emb = discord.Embed(description = 'Пользователь не в клане!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

		else:
			if cursor.execute("SELECT owner FROM clanOwners6 WHERE owner = {}".format(ctx.author.id)).fetchone() is None:

				emb = discord.Embed(description = 'Только глава может кикнуть участника с клана!')
				emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
				await ctx.send(embed = emb)

			else:
				clanName = cursor.execute("SELECT clanName FROM clanInvite17 WHERE id = {}".format(ctx.author.id)).fetchone()
				clanNameTwo = cursor.execute("SELECT clanName FROM clanInvite17 WHERE id = {}".format(member.id)).fetchone()

				if clanName == clanNameTwo:
					name = cursor.execute("SELECT clanName FROM clanInvite17 WHERE id = {}".format(ctx.author.id)).fetchone()[0]
					
					cursor.execute("DELETE FROM clanInvite17 WHERE id = {}".format(member.id))
					connection.commit()

					cursor.execute("UPDATE clanOwners6 SET members = members - {} WHERE clanName = '{}'".format(1, name))
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
	if cursor.execute("SELECT clanName FROM clanInvite17 WHERE id = {}".format(ctx.author.id)).fetchone() is None:
			
		emb = discord.Embed(description = 'Вы не в клане!')
		emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
		await ctx.send(embed = emb)

	else:
		if cursor.execute("SELECT owner FROM clanOwners6 WHERE owner = {}".format(ctx.author.id)).fetchone() is None:

			emb = discord.Embed(description = 'Только глава может удалить клан!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

		else:
			name = cursor.execute("SELECT clanName FROM clanInvite17 WHERE id = {}".format(ctx.author.id)).fetchone()[0]
			nameTwo = cursor.execute("SELECT clanName FROM clanOwners6 WHERE owner = {}".format(ctx.author.id)).fetchone()[0]


			cursor.execute("DELETE FROM clanInvite17 WHERE clanName = '{}'".format(name))
			connection.commit()

			cursor.execute("DELETE FROM clanOwners6 WHERE clanName = '{}'".format(nameTwo))
			connection.commit()

			emb = discord.Embed(description = 'Вы успешно удалили клан!')
			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)

