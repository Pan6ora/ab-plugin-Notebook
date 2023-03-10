# Notebook

A Jupyter Notebook server inside Activity Browser.

This plugin starts a Jupyter Notebook server and display its web interface inside Activity Browser.

## Configuration

Jupyter Notebook configuration files are located in the `includes/jupyter_config` folder.

If you change the localhost port, change it also on the `plugin/layouts/tabs/right.py`.

# Activity Browser

The activity browser is an open source software for Life Cycle Assessment (LCA) that builds on top of the Brightway2 LCA framework.

Rémy Le Calloch <remy@lecalloch.net> has been working for the G-SCOP laboratory on a plugin manager to add functionalities to Activity-Browser. This repository is a template of plugin that can serve as an example to create new ones.

# QuickStart

This section will let you get the modified version of Activity Browser and add the template plugin that works as a demo.

## Get Activity Browser with plugins 

You can install and start this activity-browser version like this:

```bash
conda create -n ab -c conda-forge -c cmutel -c bsteubing -c pan6ora activity-browser-plugin-manager
conda activate ab
activity-browser
```

If you need latest changes (from both the original project and this fork) you can use the dev version:

```bash
conda create -n ab -c conda-forge -c cmutel -c bsteubing -c pan6ora activity-browser-plugin-manager-dev
conda activate ab
activity-browser
```

## Setup dev environment

You will need to have python3 and conda installed (as some dependencies are not on pip).

Then, create the environment with the following commands:

```
conda create -n local_dev -c conda-forge -c cmutel -c bsteubing -c pan6ora activity-browser-plugin-manager-dev
conda activate local_dev
conda remove --force activity-browser-plugin-manager-dev
```

This create a conda environment named `local_dev` with all Activity Browser packages, then remove the package activity-browser itself (as we are going to launch it directly from the content of this repository).

To start Activity Browser clone the repo, switch to conda environment and run `run-activity-browser.py`.

Note: don't start from `anaconda` or `anaconda-dev` branches as these are only for anaconda deployement. The best practice is to start a branch from `plugin-manager` one. If you need latest changes from the original project, start from the `master` branch and merge `plugin-manager`.

```
conda activate local_dev
python activity-browser/run-activity-browser.py
```

## Add the template plugin

Use the _Import_ button in the **Plugins** section on the left panel. Select the file `template.plugin` in this repository.

After the import is completed you should now see 2 new tabs (on in each panel) named _Template_.

Well done ! You have imported your first plugin.

The next section gives explanation on how to create your own plugins.

# Creating a plugin

If everything works you can start adding real code into the plugin.

## Coding "in place"

When developing a plugin it is painful to import it every time you wan't to test your work.

To avoid doing so an idea is to replace the plugin code in your Brightway project by a link to your development folder.

After that you will only have to restart Activity Browser to see your changes without importing the plugin over and over again.

**on Linux**

The project path should be something like `$HOME/.local/share/Brightway3`. 

Creating the link should look like:

```
rm -rf $HOME/.local/share/BrightwayX/default.xxxx/plugins/*
ln -rs ./ $HOME/.local/share/BrightwayX/default.xxxx/plugins/Template
```

**on windows**

The project path should be something like `C:\users\<user>\AppData\Local\pylca\BrightwayX`.

Delete the `\default.xxx\plugins\Template` folder and replace it by a link to your development folder.

**on OSX**

The project path should be something like `/Users/<User>/Library/Application Support/Brightway2`.

Delete the `\default.xxx\plugins\Template` folder and replace it by a link to your development folder.

## Creating the plugin file

To create the plugin itself simply create a 7z archive of the code and rename it to `your_plugin.plugin`.


