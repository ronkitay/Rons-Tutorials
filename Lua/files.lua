local function readByLine() 
	thisScript = io.open("files.lua", "r")
	local line = thisScript:read("*line")
	while (line) do
		print(line)
		line = thisScript:read("*line")
	end
	thisScript:close()
end


local function readAll()
	thisScript = io.open("files.lua", "r")
	local content = thisScript:read("*all")
	print(content)
	thisScript:close()
end

readByLine()

print("-----------------------------------------")

readAll()
