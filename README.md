# Synt - Documentation

## How to run!

### Interactive Mode
- `Interactive Mode` is an easy to try algorithms and features.
- Good and suggested for learning purposes.
- To start it(through engine):
	1. run the `main source file`(`source\main.py`) directly
	2. enter `i` or `interactive`
	3. use `Interactive Mode`
- To start it(directly):
	1. start console(cmd)
	2. run `<path_to_main_source_file> --mode interactive`
	3. use `Interactive Mode`

### File Mode
- `File Mode` is good to run files directly.
- Using console is suggested.
- To start it(through engine):
	1. run the `main source file`(`source\main.py`) directly
	2. enter `f` or `file`
	3. enter `file path`
	4. use `File Mode`
- To start it(directly):
	1. start console(cmd)
	2. run `<path_to_main_source_file> --mode file --file <run_file_path>`
	3. use `File Mode`

## Examples
- Check the `examples` folder.

## Types and Triggers

### Variable Types
- `binary` (`on`, `off`)
- `number`
- `decimal`
- `text`
- `nothing`
- `collection`

### Special Character Triggers(Special Keywords)
- `NEWLINE`: `\n`
- `INDENT`: `\t`
- `BACKSPACE`: `\b`
- `START`: `\r`
- `SPACE`: ` `
- `LEFTSQUARE`: `[`
- `RIGHTSQUARE`: `]`
- `LEFTCURLY`: `{`
- `RIGHTCURLY`: `}`
- `COMMA`: `,`
- `DOT`: `.`
- `SEMICOLON`: `;`
- `COLON`: `:`
- `EQUAL`: `=`
- `HASH`: `###`
- `QUESTION`: `?`
- `EXCLAMATION`: `!`
- `QUOTE`: `"`
- `APOSTROPHE`: `'`

### Symbolic Logic Operations
- `=`
- `!=`
- `>`
- `<`
- `>=`
- `<=`
- `<-`
- `!<-`
- `_%`
- `!_%`
- `%_`
- `!%_`

### Keyword Logic Operations
- `equals to` : `=`
- `not equals to` : `!=`
- `greater than` : `>`
- `less than` : `<`
- `greater than equal to` : `>=`
- `less than equal to` : `<=`
- `contains` : `<-`
- `does not contain` : `!<-`
- `starts with` : `_%`
- `does not start with` : `!_%`
- `ends with` : `%_`
- `does not end with` : `!%_`

### Triggers
- Special Keywords Trigger : `###`
- Variable Start Trigger : `###`
- Variable End Trigger : `###`
- Meta Trigger : `?`
- Collection Item Trigger : `%`

## Algorithms

### Comment Algorithms
- `$`
- `?`
- `>`
- `comment`

### Basic Algorithms
- `version`
- `output <output-data>`
- `input <store-variable>`
- `end`

### Debug Algorithm
- `restore`
- `warn <warning>`
- `error <error>`

### Variable Algorithms
- `meta <name> <value>`
- `var <type> <name> <value>`
- `alg <name> {content}`

### Operator Algorithms
- `add <store-variable> <data1> <data2> <...>`
- `subtract <store-variable> <data1> <data2>`
- `multiply <store-variable> <data1> <data2> <...>`
- `divide <store-variable> <data1> <data2>`
- `power <store-variable> <data1> <data2>`

### Logic Algorithms
- `check <input1> <condition> <input2> <true-algorithm> <false-algorithm>`
- `condition <input1> <condition> <input2> <true-algorithm> <false-algorithm>`

### Loop Algorithms
- `repeat <amount> <repeat-function>`
- `loop <condition-switch> <repeat-function>`

### External Resource Algorithms
- `module <module-name>`

## Call Functions and Variables

### Using Variable Values
- Use `#<variable-name>#` to access the variable value.

### Getting Items From Collection
- Use `#<collection-variable-name>#%<item-index>%` to access an item from collection.

### Calling Custom Algorithms
- Use `<algorithm-name> <return-variable> <data1> <data2> <...>`

