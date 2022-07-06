import os

if False:
    from _stubs import *

class ExternalFiles:
	'''
		The ExternalFiles class is used to handle working with both externalizing files, 
		as well as ingesting files that were previously externalized. This helps
		to minimize the amount of manual work that might need to otherise be used
		for handling external files. 
	'''
	def __init__(self, my_op):
		'''
			Stands in place of an execute dat - ensures all elements start-up correctly

			Notes
			---------

			Args
			---------
			myOp (touchDesignerOperator):
			> the operator that is loading the current extension
					
			Returns
			---------
			none		
		'''

		self.my_op 				= my_op
		self.Flash_duration 	= 4

		init_msg 				= "Save init from {}".format(my_op)
		self.Defaultcolor		= parent().pars('Defaultcolor*')
		self.Op_finder 			= op('opfind1')
		self.Extension_flag 	= parent().par.Extensionflag.val

		print(init_msg)

		return
		
	def Prompt_to_save(self, current_loc):
		'''
			The method used to save an external TOX to file

			Notes
			---------

			Args
			---------
			current_loc (str):
			> the operator that's related to the currently focused 
			> pane object. This is required to ensure that we correctly
			> grab the appropriate COMP and check to see if needs to be saved
					
			Returns
			---------
			none		
		'''

		ext_color 						= parent().pars("Extcolor*")
		msg_box_title 					= "TOX Save"
		msg_box_msg 					= "Replacing External\n\nYou are about to overwite an external TOX"
		msg_box_buttons 				= ["Cancel", "Continue"]

		sav_msg_box_title 				= "Externalize Tox"
		sav_msg_box_msg 				= "This TOX is not yet externalized\n\nWould you like to externalize this TOX?"
		sav_msg_box_buttons 			= ["No", "Yes"]

		save_msg_buttons_parent_too 	= ["No", "This COMP Only", "This COMP and the Parent"]


		# check if location is the root of the project 
		if current_loc == '/':
			# skip if we're at the root of the project
			pass

		else:
			# if we're not at the root of the project 
			
			# check if external
			if current_loc.par.externaltox != '' and 'noextern' not in current_loc.tags:
				confirmation 				=  ui.messageBox(msg_box_title, msg_box_msg + '\ncomponent: ' + current_loc.path, buttons = msg_box_buttons)

				if confirmation:

					# save external file
					self.Save_over_tox(current_loc)
				
				else:
					# if the user presses "cancel" we pass
					pass
			
			# in this case we are not external, so let's ask if we want to externalize the file
			else:

				# check if the parent is externalized
				if current_loc.parent().par.externaltox != '' and 'noextern' not in current_loc.parent().tags:
					save_ext 			= ui.messageBox(
						sav_msg_box_title,
						sav_msg_box_msg +
						'\nparent: ' + current_loc.parent().path +
						'\ncomponent: ' + current_loc.path,
						buttons = save_msg_buttons_parent_too)

					# save this comp only
					if save_ext == 1:
						self.Save_tox(current_loc)

					# save this comp and the parent
					elif save_ext == 2:
						self.Save_tox(current_loc)
						print("save this tox")

						# save parent() COMP
						self.Save_over_tox(current_loc.parent())
						print("Save the parent too!")

					# user selected 'No'
					else:
						pass

				# the parent is not external, so let's ask about externalizing the tox
				elif 'noextern' not in current_loc.tags:
					save_ext 			= ui.messageBox(sav_msg_box_title, sav_msg_box_msg + '\ncomponent: ' + current_loc.path, buttons = sav_msg_box_buttons)
					
					if save_ext:
						self.Save_tox(current_loc)

					else:
						# the user selected "No"
						pass

		
		return

	def Save_over_tox(self, current_loc):
		ext_color 				= parent().pars("Extcolor*")
		external_path 			= current_loc.par.externaltox
		current_loc.save(external_path)

		# set color for COMP
		current_loc.color 		= (ext_color[0], ext_color[1], ext_color[2])

		# flash color
		self.Flash_bg("Bgcolor")

		# create and print log message
		log_msg 		= "{} saved to {}/{}".format(current_loc, 
													project.folder, 
													external_path)
		
		self.Logtotextport(log_msg)

		return

	def Save_tox(self, current_loc):
		ext_color 				= parent().pars("Extcolor*")

		# ask user for a save location
		save_loc 		= ui.chooseFolder(title="TOX Location", start=project.folder)
		
		# construct a relative path and relative loaction for our elements
		print(save_loc)
		rel_path 		= tdu.collapsePath(save_loc)
		
		# check to see if the location is at the root of the project folder structure
		if rel_path == "$TOUCH":
			rel_loc 	= '{new_tox}/{new_tox}.tox'.format(new_tox = current_loc.name)
		
		# save path is not in the root of the project
		else:
			rel_loc 	= '{new_module}/{new_tox}/{new_tox}.tox'.format(new_module = rel_path, new_tox = current_loc.name)

		# create path and directory in the OS
		new_path 		= '{selected_path}/{new_module}'.format(selected_path = save_loc, new_module = current_loc.name)
		os.mkdir(new_path)

		# format our tox path
		tox_path 		= '{dir_path}/{tox}.tox'.format(dir_path = new_path, tox = current_loc.name)

		# setup our module correctly
		current_loc.par.externaltox 		= rel_loc
		current_loc.par.savebackup 			= False

		# set color for COMP
		current_loc.color 		= (ext_color[0], ext_color[1], ext_color[2])

		# save our tox
		current_loc.save(tox_path)

		# flash color
		self.Flash_bg("Bgcolor")

		# create and print log message
		log_msg 		= "{} saved to {}/{}".format(current_loc, 
													project.folder, 
													tox_path)
		self.Logtotextport(log_msg)
		return

	def Reload_ext_dat(self, external_file):
		return
		'''
			Used to reload DAT files, and to re-init modules. 

			Notes
			---------

			Args
			---------
			external_file (str):
			> the operator that's related to the currently focused 
			> pane object. This is required to ensure that we correctly
			> grab the appropriate COMP and check to see if needs to be saved
					
			Returns
			---------
			none		
		'''

		file_path 			= '{project}/{file}'.format(project=project.folder, file=external_file)

		# loop through all the dats
		for each_op in self.Op_finder.cols(2)[0][1:]:
			each_op_path 		= op(each_op).par.file.val
			# print( file_path == each_op_path)

			# check our file path to see if it's relative or absolute
			# change our path if we need to
			if os.path.isabs(each_op_path):
				pass
			else:
				each_op_path = '{}/{}'.format(project.folder, each_op_path)
			
			# if there's a match reload the DAT
			if file_path == each_op_path:
				op(each_op.val).par.loadonstartpulse.pulse()
				
				# flash the background so we know a file has been loaded
				self.Flash_bg("Savecolor")

				# check to see if the external file is python
				if external_file.split('.')[1] == "py":

					# check to see if an op is flagged as an extension:
					if self.Extension_flag in op(each_op.val).tags:

						# check to see the op's parent has any extensions
						extension_pars = [ext for ext in op(each_op.val).parent().pars('extension*')]
						if len(extension_pars) > 0:
							# print(op(each_op.val).parent())

							# reinit the parent's extensions
							op(each_op.val).parent().par.reinitextensions.pulse()

						elif op(each_op.val).parent().isCOMP and op(each_op.val).parent().par.externaltox != '':
							# print("This needs reinit")
						
							# if the DAT has a parent COMP, reinit the extension
							op(each_op.val).parent().par.reinitextensions.pulse()

							self.Flash_bg("Savecolor")
						
						else:
							# COMP is the only consideration we care about at the moment
							pass
				else:
					# skip other file types for now
					pass

				# stop once we have a hit
				break

			else:
				pass

		return

	def Flash_bg(self, parColors):
		'''
			Used to flash the background of the TD network. 

			Notes
			---------
			This is a simple tool to flash indicator colors in the
			background to help you have some visual confirmation that
			you have in fact externalized a file.

			Args
			---------
			parColors (str):
			> this is the string name to match against the parent's pars()
			> for to pull colors to use for changing the background
					
			Returns
			---------
			none		
		'''
		par_color 			= '{}*'.format(parColors)
		over_ride_color 	= parent().pars(par_color)

		# change background color (0.1, 0.105, 0.12)
		ui.colors['worksheet.bg'] 	= over_ride_color
		delay_script 				= "ui.colors['worksheet.bg'] = args[0]"
		
		# want to change the background color back
		run(delay_script, self.Defaultcolor, delayFrames = self.Flash_duration)		

		return

	def Logtotextport(self, logMsg):

		if parent().par.Logtotextport:
			print(logMsg)

		else:
			pass

		return	