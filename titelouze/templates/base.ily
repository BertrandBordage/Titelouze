\version "{{ self.lilypond_version }}"

\paper {
  print-all-headers = ##t
}

{{ self.book }}
