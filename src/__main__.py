def main():
  args = cli.parse_args()
  if args.has_explicit_target():
    request = cli.build_request(args)
  else:
    request = tui.selector.run()
  data = fastf1_client.load(request)
  figure = plotting.render(data, request.mode)
  export.output(figure, request)