import { chmodSync, lstatSync, mkdirSync } from "node:fs"

const root = "/tmp/opencode"

// Plugin initialization runs at startup, before tools use the private directory.
export default async () => {
  try {
    mkdirSync(root, { mode: 0o700 })
  } catch (error) {
    if ((error as { code?: string }).code !== "EEXIST") throw error
  }
  const info = lstatSync(root)
  if (!info.isDirectory() || info.uid !== process.getuid?.()) {
    throw new Error(`unsafe temporary directory: ${root}`)
  }
  chmodSync(root, 0o700)
  process.env.TMPDIR = root

  return {
    "shell.env": async (_input: unknown, output: { env: Record<string, string> }) => {
      output.env.TMPDIR = root
    },
  }
}
