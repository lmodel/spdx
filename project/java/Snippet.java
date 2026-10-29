package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Describes a certain part of a file.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Snippet extends SoftwareArtifact {

  private PositiveIntegerRange byteRange;
  private PositiveIntegerRange lineRange;
  private File snippetFromFile;


}