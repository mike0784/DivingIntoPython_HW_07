def read_and_write_files(name_file_names: str,
                         name_file_nambers: str,
                         name_file_output: str) -> None:

    with (open(name_file_names, 'r', encoding='utf-8') as file_names,
          open(name_file_nambers, 'r', encoding='utf-8') as file_nambers):
        names = file_names.read().split('\n')
        nambers = file_nambers.read().split('\n')
    
    if len(nambers) > len(names):
        names += names[:len(nambers)-len(names)]
    else:
        nambers += nambers[:len(names)-len(nambers)]

    with (open(name_file_output, 'w', encoding='utf-8') as file_output):
        for name, namber in zip(names, nambers):

            if not name or not namber:
                break

            namber_output_int, namber_output_float = map(float, namber.split(' | '))

            multik: float = namber_output_int * namber_output_float

            if multik < 0:
                file_output.write(f"{name.lower()} {abs(multik)} \n")
            else:
                file_output.write(f"{name.upper()} {int(multik)} \n")