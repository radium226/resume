SHELL=/bin/bash
.SHELLFLAGS = -e -u -c
.ONESHELL:

BUILD_FOLDER := build

$(BUILD_FOLDER)/Expériences_professionnelles.md:
	mkdir -p '$(BUILD_FOLDER)'
	{
		cat 'markdown/Expériences_professionnelles/En_tête.md'
		find 'markdown/Expériences_professionnelles' -type "d" -print | grep -vE 'Expériences_professionnelles$$' | sort -r | while read folder_path; do
			cat "$${folder_path}/En_tête.md"
			echo
			find "$${folder_path}" -type "f" -name "*.md" -print | grep -vE 'En_tête.md$$' | sort -r | xargs -I {} bash -c "cat '{}' && echo"
		done
	} >'$(BUILD_FOLDER)/Expériences_professionnelles.md'

$(BUILD_FOLDER)/CV.md: $(BUILD_FOLDER)/Expériences_professionnelles.md
	mkdir -p '$(BUILD_FOLDER)'
	{
		cat 'markdown/En_tête.md'
		echo
		cat '$(BUILD_FOLDER)/Expériences_professionnelles.md'
		echo
	} >'$(BUILD_FOLDER)/CV.md'

$(BUILD_FOLDER)/CV.html: $(BUILD_FOLDER)/CV.md
	mkdir -p '$(BUILD_FOLDER)'
	# I don't know why, but --data-dir does not work
	XDG_DATA_HOME='$(PWD)' \
		pandoc \
			--template='CV' \
			--verbose \
			--from='markdown' \
			--to='html' \
			--output='$(BUILD_FOLDER)/CV.html' \
			'$(BUILD_FOLDER)/CV.md'

.PHONY: build
build: $(BUILD_FOLDER)/CV.html

.PHONY: clean
clean:
	test -d '$(BUILD_FOLDER)' && rm -Rf '$(BUILD_FOLDER)' || true

.PHONY: open
open: $(BUILD_FOLDER)/CV.html
	firefox '$(BUILD_FOLDER)/CV.html'
