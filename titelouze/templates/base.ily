\version "{{ self.lilypond_version }}"

\pointAndClickOff
#(set-global-staff-size {{ self.book.staff_size }})

\paper {
  print-all-headers = ##t
  {{ self.book.paper_properties }}
}

{{ self.book }}
