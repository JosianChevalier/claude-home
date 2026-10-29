import { tool } from "@opencode-ai/plugin"

// OpenCode's side of tools/run: the session id reaches the shell only through a tool's context.
export default tool({
  description: "Run a harness tool; `run doc opencode` prints every tool's help. The project's tools/<name> comes first, then the home's.",
  args: {
    name: tool.schema.string().describe("the tool"),
    args: tool.schema.string().optional().describe("its arguments, as written on a shell line"),
  },
  async execute({ name, args }, context) {
    const out = await Bun.$`${import.meta.dir}/run ${name} ${{ raw: args ?? "" }}`
      .env({ ...process.env, OPENCODE_SESSION_ID: context.sessionID })
      .cwd(context.directory)
      .nothrow()
    return (out.stdout.toString() + out.stderr.toString()).trim()
  },
})
